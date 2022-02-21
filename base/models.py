from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    sku = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    collection = models.CharField(max_length=200, null=True, blank=True)
    imageAmount = models.CharField(max_length=200, null=True, blank=True)
    videoAmount = models.CharField(max_length=200, null=True, blank=True)
    videoWidth = models.IntegerField(null=True, blank=True, default=0)
    videoHeight = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(null=True, blank=True)
    descriptionSmall = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.IntegerField(null=True, blank=True, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

