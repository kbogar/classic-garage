from django.db import models
from cloudinary.models import CloudinaryField


class services(models.Model):
    """
    This defines the Services Model, with a featured image,
    a title, brief description, and a price.
    """
    image = CloudinaryField('image')
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)
