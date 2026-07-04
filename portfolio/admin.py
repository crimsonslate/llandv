from django.contrib import admin

from . import models


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.GalleryPost)
class GalleryPostAdmin(admin.ModelAdmin):
    pass
