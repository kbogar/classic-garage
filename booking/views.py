from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CustomContactForm, BookingModelForm
from .models import BookingModel
from django.views.generic.edit import FormView
from django.contrib import messages
from django.http import HttpResponseRedirect


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class OurServices(TemplateView):
    template_name = 'our_services.html'


class BookService(CreateView):
    """
    Handels the booking form page. After submitting the
    form, the user will be redirected to my bookings page.
    """
    template_name = 'book_service.html'
    form_class = BookingModelForm
    success_url = '/my_bookings/'

    def form_valid(self, form):
        form.instance.customer = self.request.user
        form.save()
        messages.success(
            self.request,
            "Your booking has been created successfully!")
        return super().form_valid(form)


class MyBooking(generic.ListView):
    """
    Handels my bookings page, with the logged in users
    booking data.
    """
    model = BookingModel
    template_name = 'my_bookings.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = context['object_list']
        return context

    def get_queryset(self):
        user = self.request.user
        return BookingModel.objects.filter(customer=user)


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
