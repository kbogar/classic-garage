from django.shortcuts import render, redirect
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
    Handels the Contact Page, with a message.
    """
    template_name = 'contact.html'
    form_class = CustomContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form = form.save(commit=False)
        form.save()
        messages.success(
            self.request,
            "Thank you for reaching out to us. We'll be in touch soon.")
        return super().form_valid(form)
