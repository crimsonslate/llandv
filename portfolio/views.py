from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_http_methods
from django.views.decorators.vary import vary_on_headers

from llandv.decorators import htmx_template

from portfolio.forms import ContactForm
from portfolio.models import Gallery, GalleryPost


@vary_on_headers("HX-Request")
@require_GET
@htmx_template("portfolio/home.html")
def home_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@require_GET
@htmx_template("portfolio/about.html")
def about_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@require_GET
@htmx_template("portfolio/contact.html")
def contact_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@require_http_methods(["GET", "POST"])
@htmx_template("portfolio/contact_form.html")
def contact_form_view(request: HttpRequest) -> HttpResponse:
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("portfolio:contact form success")
    return TemplateResponse(request, request.template_name, {"form": form})


@vary_on_headers("HX-Request")
@require_GET
@htmx_template("portfolio/contact_form_success.html")
def contact_form_success_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@require_GET
@htmx_template("portfolio/gallery.html")
def gallery_view(
    request: HttpRequest, gallery_pk: int, gallery_slug: str
) -> HttpResponse:
    gallery = get_object_or_404(Gallery, pk=gallery_pk, slug=gallery_slug)
    return TemplateResponse(
        request,
        request.template_name,
        {"gallery": gallery, "posts": gallery.posts.all()},
    )


@require_GET
@htmx_template("portfolio/post.html")
def post_view(
    request: HttpRequest, gallery_pk: int, gallery_slug: str, post_pk: int
) -> HttpResponse:
    gallery = get_object_or_404(Gallery, pk=gallery_pk, slug=gallery_slug)
    post = get_object_or_404(gallery.posts.all(), pk=post_pk)
    return TemplateResponse(request, request.template_name, {"post": post})
