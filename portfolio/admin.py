from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from . import models


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"
    prepopulated_fields = {"slug": ["name"]}


@admin.register(models.Post)
class PostAdmin(OrderedModelAdmin):
    list_display = ["caption", "move_up_down_links"]
    list_filter = ["gallery"]


@admin.register(models.ContactResponse)
class ContactResponseAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"
