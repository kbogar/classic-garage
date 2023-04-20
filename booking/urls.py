from django.urls import path
from . import views
from .views import Home, About, OurServices, BookService,\
     Contact, UpdateBooking


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('our_services/', OurServices.as_view(), name='our_services'),
    path('book_service/', BookService.as_view(), name='book_service'),
    path('my_bookings/', UpdateBooking.as_view(), name='my_bookings'),
    path('contact/', Contact.as_view(), name='contact'),
]
