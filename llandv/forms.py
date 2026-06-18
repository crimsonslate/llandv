from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(max_length=2048, widget=forms.widgets.Textarea())
