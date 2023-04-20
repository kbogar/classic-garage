from django import forms
from .models import CustomModel
from django.forms import ModelForm


class CustomContactForm(forms.ModelForm):
    """
    Handels the contact form.
    """
    class Meta:
        model = CustomModel
        fields = '__all__'
