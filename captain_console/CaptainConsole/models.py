from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    manufacturer = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    mainImageLink = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    imageLink = models.CharField(max_length=255)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviewTitle = models.CharField(max_length=255)
    reviewText = models.CharField(max_length=999)
    datetime = models.DateTimeField()

class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)
    country = CountryField(blank_label='(select country)')

class PaymentAndShipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameoncard = models.CharField(max_length=50)
    creditcardnumber = models.CharField(max_length=16)
    expirationdate = models.CharField(max_length=50)
    cvv = models.IntegerField()
    shippingcompany = models.CharField(max_length=50)
    shippingoption = models.CharField(max_length=50)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=6)
    country = models.CharField(max_length=50)
    nameoncard = models.CharField(max_length=50)
    creditcardnumber = models.CharField(max_length=16)
    expirationdate = models.CharField(max_length=50)
    cvv = models.IntegerField()
    price = models.FloatField()
    orderitems = models.CharField(max_length=9999)
    shippingcompany = models.CharField(max_length=50)
    shippingoption = models.CharField(max_length=50)
    additionalinfo = models.CharField(max_length=999, blank= True)

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    searchQuery = models.CharField(max_length=255)
    datetime = models.DateTimeField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_image = models.CharField(max_length=9999)

class PreviouslyViewed(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()