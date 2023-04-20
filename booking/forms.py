from django import forms
from .models import CustomModel, BookingModel
from django.forms import ModelForm


class BookingModelForm(forms.ModelForm):
    """
    Handels the book service form.
    """
    class Meta:
        model = BookingModel
        fields = ('name', 'email', 'created_on', 'service_type', 'message')


class CustomContactForm(forms.ModelForm):
    """
    Handels the contact form.
    """
    class Meta:
        model = CustomModel
        fields = '__all__'
