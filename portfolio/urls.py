from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("contact/form/", views.contact_form_view, name="contact form"),
    path(
        "contact/form/success/",
        views.contact_form_success_view,
        name="contact form success",
    ),
    path(
        "galleries/<int:gallery_pk>.<str:gallery_slug>/",
        views.gallery_view,
        name="gallery",
    ),
    path(
        "galleries/<int:gallery_pk>.<str:gallery_slug>/<int:post_pk>/",
        views.post_view,
        name="post",
    ),
]
