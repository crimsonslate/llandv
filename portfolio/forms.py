from django import forms
from django.utils.translation import gettext_lazy as _

from portfolio.models import ContactFormResponse


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormResponse
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.widgets.TextInput(
                attrs={
                    "autocomplete": "name",
                    "placeholder": "johnny appleseed",
                    "autofocus": "on",
                }
            ),
            "email": forms.widgets.EmailInput(
                attrs={
                    "autocomplete": "email",
                    "placeholder": "johnny@apple.com",
                }
            ),
            "message": forms.widgets.Textarea(attrs={"autocomplete": "on"}),
        }
