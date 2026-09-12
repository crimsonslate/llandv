from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.contrib.settings.models import (
    register_setting,
    BaseGenericSetting,
)


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


class AboutPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("body")]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration")
    ]


class GalleryIndexPage(Page):
    pass


class GalleryPage(Page):
    pass


class ContactPage(Page):
    pass
