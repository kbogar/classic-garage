from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import CustomContactForm
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        messages.success(
            self.request,
            "Thank you for reaching out to us. We'll be in touch soon.")
        return super().form_valid(form)


class ContactSucces(TemplateView):
    template_name = 'contact_success.html'


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was \
             an error loggin in, Try again.")
            return redirect('login')

    else:
        return render(request, 'account/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')
