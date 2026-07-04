from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Gallery(models.Model):
    name = models.CharField(max_length=256, unique=True)
    desc = models.TextField(blank=True, max_length=2048)
    slug = models.SlugField(blank=True)
    posts = models.ManyToManyField(
        "portfolio.GalleryPost", blank=True, related_name="galleries"
    )

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _("galleries")

    def __str__(self) -> str:
        return self.name

    def save(self, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(**kwargs)

    def get_absolute_url(self) -> str:
        return reverse(
            "portfolio:gallery",
            kwargs={"gallery_pk": self.pk, "gallery_slug": self.slug},
        )


class GalleryPost(models.Model):
    file = models.FileField()
    caption = models.CharField(max_length=256)
    desc = models.TextField(blank=True, max_length=2048)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self) -> str:
        return self.caption


class ContactFormResponse(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    message = models.TextField(max_length=2048)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("contact form response")
        verbose_name_plural = _("contact form responses")

    def __str__(self) -> str:
        return self.name
