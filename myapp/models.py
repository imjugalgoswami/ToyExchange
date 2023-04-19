
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import truncatechars

class Ad(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='media', null=True, blank=True)
    image2 = models.ImageField(upload_to='media', null=True, blank=True)
    image3 = models.ImageField(upload_to='media', null=True, blank=True)
    image4 = models.ImageField(upload_to='media', null=True, blank=True)
    image5 = models.ImageField(upload_to='media', null=True, blank=True)
    image6 = models.ImageField(upload_to='media', null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    short_description = property(lambda self: truncatechars(self.description, 10))

    def __str__(self):
        return self.title



