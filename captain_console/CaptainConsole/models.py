from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=999)
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    admin = models.BooleanField()

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    manufacturer = models.CharField(max_length=255)
    mainImage = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    imageFileName = models.CharField(max_length=255)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField()
    reviewTitle = models.CharField(max_length=255)
    reviewText = models.CharField(max_length=999)
    datetime = models.DateTimeField(max_length=255)

class ShoppingCart(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    productIDs = models.CharField(max_length=999)
    productAmount = models.CharField(max_length=999)

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    shoppingCart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.FloatField()
    additionalInfo = models.CharField(max_length=999, blank= True)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class SearchHistory(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    keywordIDs = models.CharField(max_length=999)
    searchQuery = models.CharField(max_length=255)
    datetime = models.DateTimeField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=9999)
