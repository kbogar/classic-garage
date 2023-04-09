from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'Pending'), (1, 'Approved'))


class BookingModel(models.Model):
    """
    This defines the Booking Model
    """
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')