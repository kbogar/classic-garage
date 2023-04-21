from django.urls import path
from . import views
from .views import Home, About, OurServices, BookService,\
     Contact, MyBooking, UpdateBooking, DeleteBooking


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('our_services/', OurServices.as_view(), name='our_services'),
    path('book_service/', BookService.as_view(), name='book_service'),
    path('my_bookings/', MyBooking.as_view(), name='my_bookings'),
    path('update_bookings/<int:pk>', UpdateBooking.as_view(),
         name='update_bookings'),
    path('delete_bookings/<int:pk>',
         DeleteBooking.as_view(), name='delete_bookings'),
    path('contact/', Contact.as_view(), name='contact'),
]
