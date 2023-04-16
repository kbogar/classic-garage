from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CustomContactForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.http import HttpResponseRedirect


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class OurServices(TemplateView):
    template_name = 'our_services.html'


class BookService(TemplateView):
    template_name = 'book_service.html'


class Contact(FormView):
    """
    Handels the Contact Page
    """
    template_name = 'contact.html'
    form_class = CustomContactForm
    success_url = '/contact_success/'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.save()
        return super().form_valid(form)


class ContactSucces(TemplateView):
    template_name = 'contact_success.html'
