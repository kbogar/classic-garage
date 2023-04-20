from django import forms
from .models import CustomModel, BookingModel
from django.forms import ModelForm
import datetime


class DateInput(forms.DateInput):
    """
    This widget provides a way to select a date from a graphical calendar.
    from https://webpedia.net/how-to-use-datepicker-in-django
    """
    input_type = 'date'


class BookingModelForm(forms.ModelForm):
    """
    Handels the book service form.
    """
    class Meta:
        model = BookingModel
        fields = ('name',
                  'email',
                  'created_on',
                  'service_type',
                  'message',)
        widgets = {
            'created_on': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=3),
                'max': datetime.date.today()+datetime.timedelta(days=60),
            })
        }


class CustomContactForm(forms.ModelForm):
    """
    Handels the contact form.
    """
    class Meta:
        model = CustomModel
        fields = '__all__'
