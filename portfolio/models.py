from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.forms import FormBuilder
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    FieldRowPanel,
)
from wagtail.blocks import ListBlock, RichTextBlock
from wagtail.contrib.settings.models import (
    register_setting,
    BaseGenericSetting,
)
from wagtail.fields import StreamField, RichTextField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


@register_setting
class NavigationSettings(BaseGenericSetting):
    instagram_url = models.URLField(
        verbose_name=_("Instagram URL"), blank=True
    )
    tiktok_url = models.URLField(verbose_name=_("TikTok URL"), blank=True)
    youtube_url = models.URLField(verbose_name=_("YouTube URL"), blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("instagram_url"),
                FieldPanel("tiktok_url"),
                FieldPanel("youtube_url"),
            ],
            _("Social Settings"),
        )
    ]


class HomePage(Page):
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel("hero_image"),
    ]

    def get_context(self, request, *args, **kwargs) -> dict:
        context = super().get_context(request, *args, **kwargs)
        context["latest_galleries"] = []
        return context


class StandardPage(Page):
    body = RichTextField(features=["h2", "bold", "italic", "link", "image"])

    content_panels = Page.content_panels + [FieldPanel("body")]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration")
    ]


class GalleryIndexPage(Page):
    featured_gallery = models.ForeignKey(
        "portfolio.GalleryPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [FieldPanel("featured_gallery")]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration")
    ]

    def get_context(self, request, *args, **kwargs) -> dict:
        context = super().get_context(request, *args, **kwargs)
        context["galleries"] = GalleryPage.objects.child_of(self).live()
        return context


class GalleryPage(Page):
    parent_page_types = ["portfolio.GalleryIndexPage"]

    pub_date = models.DateField(default=datetime.today)
    body = StreamField(
        [
            ("description", RichTextBlock(blank=True)),
            ("carousel", ListBlock(ImageChooserBlock(), max_num=24)),
        ],
        blank=True,
        block_counts={
            "description": {"max_num": 1},
            "carousel": {"max_num": 1},
        },
    )

    content_panels = Page.content_panels + [
        FieldPanel("pub_date"),
        FieldPanel("body"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration")
    ]

    @property
    def thumbnail(self):
        carousel = self.body.blocks_by_name("carousel")[0]
        return carousel.value[0] if carousel.value else None


class FormField(AbstractFormField):
    page = ParentalKey(
        "FormPage", on_delete=models.CASCADE, related_name="form_fields"
    )
    placeholder = models.CharField(blank=True, max_length=256)

    panels = AbstractFormField.panels + [FieldPanel("placeholder")]


class PortfolioFormBuilder(FormBuilder):
    def get_create_field_function(self, type):
        create_field_function = super().get_create_field_function(type)

        def wrapped_create_field_function(field, options):
            created_field = create_field_function(field, options)
            created_field.widget.attrs.update(
                {"placeholder": field.placeholder}
            )
            return created_field

        return wrapped_create_field_function


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [FieldPanel("from_address"), FieldPanel("to_address")]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]
