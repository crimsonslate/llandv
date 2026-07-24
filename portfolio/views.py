from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET, require_http_methods
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.cache import cache_control

from llandv.decorators import HttpRequest, htmx_template

from portfolio.forms import ContactResponseForm
from portfolio.models import Gallery


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/home.html")
def home_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/about.html")
def about_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/contact.html")
def contact_view(request: HttpRequest) -> HttpResponse:
    form = ContactResponseForm()
    return TemplateResponse(request, request.template_name, {"form": form})


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_http_methods(["GET", "POST"])
@htmx_template("portfolio/contact_form.html")
def contact_form_view(request: HttpRequest) -> HttpResponse:
    form = ContactResponseForm()
    if request.method == "POST":
        form = ContactResponseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("portfolio:contact form success")
    return TemplateResponse(request, request.template_name, {"form": form})


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/contact_form_success.html")
def contact_form_success_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/gallery_list.html")
def gallery_list_view(request: HttpRequest) -> HttpResponse:
    gallery_list = Gallery.objects.get_all_ordered_by_pub_date_ascending()
    return TemplateResponse(
        request, request.template_name, {"gallery_list": gallery_list}
    )


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/gallery_detail.html")
def gallery_detail_view(
    request: HttpRequest, gallery_pk: int, gallery_slug: str
) -> HttpResponse:
    gallery = get_object_or_404(Gallery, pk=gallery_pk, slug=gallery_slug)
    return TemplateResponse(
        request,
        request.template_name,
        {"gallery": gallery, "posts": gallery.posts.filter()},
    )


@vary_on_headers("HX-Request")
@cache_control(max_size=300)
@require_GET
@htmx_template("portfolio/post_detail.html")
def post_detail_view(
    request: HttpRequest, gallery_pk: int, gallery_slug: str, post_pk: int
) -> HttpResponse:
    gallery = get_object_or_404(Gallery, pk=gallery_pk, slug=gallery_slug)
    post = get_object_or_404(gallery.posts.filter(), pk=post_pk)
    return TemplateResponse(
        request, request.template_name, {"gallery": gallery, "post": post}
    )
