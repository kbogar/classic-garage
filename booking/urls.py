from django.urls import path
from . import views
from .views import Home, About, OurServices, BookService, Contact
from .views import ContactSucces


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('our_services/', OurServices.as_view(), name='our_services'),
    path('book_service/', BookService.as_view(), name='book_service'),
    path('contact/', Contact.as_view(), name='contact'),
    path('contact_success/', ContactSucces.as_view(), name='contact_success'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
]
