from django import forms
from django.utils.translation import gettext_lazy as _

from portfolio.models import ContactResponse


class ContactResponseForm(forms.ModelForm):
    class Meta:
        model = ContactResponse
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.widgets.TextInput(
                attrs={
                    "autocomplete": "name",
                    "placeholder": "full name",
                    "autofocus": "on",
                }
            ),
            "email": forms.widgets.EmailInput(
                attrs={
                    "autocomplete": "email",
                    "placeholder": "email@domain.com",
                }
            ),
            "message": forms.widgets.Textarea(
                attrs={"autocomplete": "on", "placeholder": "let's work"}
            ),
        }
