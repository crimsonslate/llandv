from django.db import models
from django.urls import reverse
from datetime import date
from django.utils.translation import gettext_lazy as _
from ordered_model.models import OrderedModel, OrderedModelBase


class GalleryQuerySet(models.QuerySet):
    def get_all_ordered_by_pub_date_ascending(self):
        return self.order_by("pub_date")


class Gallery(models.Model):
    name = models.CharField(max_length=256, unique=True)
    desc = models.TextField(blank=True, max_length=2048)
    slug = models.SlugField()
    pub_date = models.DateField(default=date.today)
    objects = GalleryQuerySet.as_manager()

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _("galleries")
        ordering = ("pub_date",)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            "portfolio:gallery detail",
            kwargs={"gallery_pk": self.pk, "gallery_slug": self.slug},
        )

    def get_thumbnail_url_for_first_post(self):
        if self.posts.count() > 0:
            return self.posts.get_queryset().first().file.url


class Post(OrderedModelBase):
    gallery = models.ForeignKey(
        "portfolio.Gallery", on_delete=models.CASCADE, related_name="posts"
    )
    file = models.ImageField()
    caption = models.CharField(max_length=256)
    desc = models.TextField(blank=True, max_length=2048)
    sort_order = models.PositiveIntegerField(editable=False, db_index=True)
    order_field_name = "sort_order"
    order_with_respect_to = "gallery"

    class Meta(OrderedModel.Meta):
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ("gallery", "sort_order")

    def __str__(self) -> str:
        return self.caption

    def get_absolute_url(self) -> str:
        return reverse(
            "portfolio:post detail",
            kwargs={
                "gallery_pk": self.gallery.pk,
                "gallery_slug": self.gallery.slug,
                "post_pk": self.pk,
            },
        )


class ContactResponse(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    message = models.TextField(max_length=2048)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("contact response")
        verbose_name_plural = _("contact responses")

    def __str__(self) -> str:
        return self.name
