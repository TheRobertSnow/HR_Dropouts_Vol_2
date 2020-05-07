from django.db import models

# Create your models here.
class Users(models.Model):
    password = models.CharField(max_length=255) # passa hash
    avatar = models.CharField(max_length=999) # pic within the database ?? idunno
    nickname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    admin = models.BooleanField()

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=999)
    manufacturer = models.CharField(max_length=255)

class ProductImages(models.Model):
    imageFileName = models.CharField(max_length=999)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)

class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField()
    reviewText = models.CharField(max_length=999) # meira ? idunno

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
    searchQuery = models.CharField(max_length=255) #sentance
    datetime = models.DateTimeField(max_length=255)
