from django.db import models
from django.contrib.auth.models import User
from services.models import Service

STATUS = ((0, 'Pending'), (1, 'Approved'))


class BookingModel(models.Model):
    """
    This defines the Booking Model, the fielad are needed
    for the customer to make a booking.
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    created_on = models.DateField()
    updated_on = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=400, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    admin_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.name)
