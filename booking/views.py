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
    succes_url = '/contact/'

    def form_valid(self, form):
        form.object()
        messages.success(
            self.request,
            "Thank you for reaching out! We value your inquiry \
            and will respond as soon as we can.")
        return HttpResponseRedirect(self.request.path_info)
