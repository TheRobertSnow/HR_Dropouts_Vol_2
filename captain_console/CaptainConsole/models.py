from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    manufacturer = models.CharField(max_length=255)
    mainImageLink = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    imageLink = models.CharField(max_length=255)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField()
    reviewTitle = models.CharField(max_length=255)
    reviewText = models.CharField(max_length=999)
    datetime = models.DateTimeField()

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.FloatField()
    additionalInfo = models.CharField(max_length=999, blank= True)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    keywordIDs = models.CharField(max_length=999)
    searchQuery = models.CharField(max_length=255)
    datetime = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=9999)

class PreviouslyViewed(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
