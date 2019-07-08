from django import forms
from .models import ContactFormModel


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = [
            "name", "email",
            "phone", "message"
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Adress"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Message"
            })
        }

        labels = {
            "name": "Name",
            "email": "Email Adress",
            "phone": "Phone Number",
            "message": "Message"
        }