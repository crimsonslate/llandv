from django.core.mail import send_mail
from django.http import HttpRequest as HttpRequestBase
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import timezone
from django.shortcuts import redirect
from django.views.decorators.cache import cache_control, never_cache
from django.views.decorators.http import require_GET, require_http_methods
from django.views.decorators.vary import vary_on_headers
from django.template.loader import render_to_string

from llandv.decorators import htmx_template
from llandv import forms


class HttpRequest(HttpRequestBase):
    template_name: str


@vary_on_headers("HX-Request")
@cache_control(max_age=300)
@require_GET
@htmx_template("llandv/home.html")
def home_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@cache_control(max_age=300)
@require_GET
@htmx_template("llandv/about.html")
def about_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@cache_control(max_age=300)
@require_GET
@htmx_template("llandv/contact.html")
def contact_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)


@vary_on_headers("HX-Request")
@never_cache
@require_http_methods(["GET", "POST"])
@htmx_template("llandv/contact_form.html")
def contact_form_view(request: HttpRequest) -> HttpResponse:
    form = forms.ContactForm()
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email_template_name = "llandv/emails/contact_form_response.txt"
            email_context = form.cleaned_data | {"date": timezone.now()}
            send_mail(
                subject="llandv.com Contact Form Response",
                message=render_to_string(email_template_name, email_context),
                from_email="noreply@llandv.com",
                recipient_list=["bryce@llandv.com"],
                fail_silently=True,
            )
            return redirect("contact form success")
    return TemplateResponse(request, request.template_name, {"form": form})


@vary_on_headers("HX-Request")
@cache_control(max_age=300)
@require_GET
@htmx_template("llandv/contact_form_success.html")
def contact_form_success_view(request: HttpRequest) -> HttpResponse:
    return TemplateResponse(request, request.template_name)
