from django import forms
from .models import CustomModel
from django.forms import ModelForm


# class CustomContactForm(forms.ModelForm):
#     """
#     This form interacts with Custom Model to
#     handle contact form
#     """
#     class Meta:
#         model = CustomModel
#         fields = ('name', 'email', 'message',)

#     def object(self):
#         pass
class CustomContactForm(forms.ModelForm):
    class Meta:
        model = CustomModel
        fields = '__all__'
