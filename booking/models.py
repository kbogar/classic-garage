from django.db import models
from django.contrib.auth.models import User
from .constants import TYPE_SERVICES


STATUS = ((0, 'Pending'), (1, 'Approved'))


class BookingModel(models.Model):
    """
    This defines the Booking Model, the field are needed
    for the customer to make a booking.
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='booking')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    created_on = models.DateField()
    updated_on = models.DateTimeField(auto_now=True)
    service_type = models.CharField(
        max_length=15, choices=TYPE_SERVICES, default='OT')
    message = models.TextField(max_length=400, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    admin_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.name)


class CustomModel(models.Model):
    """
    This defines the Custom Model, with contact details
    form.
    """
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField(max_length=400, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
