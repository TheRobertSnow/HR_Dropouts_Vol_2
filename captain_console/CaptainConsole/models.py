from django.db import models

# Create your models here.
class Users(models.Model):
    password = models.CharField(max_length = 255) # passa hash
    avatar = models.IntegerField() # pic within the database ?? idunno
    nickname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    admin = models.BooleanField()


class Products(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.CharField(max_length = 999)
    manufacturer = models.CharField(max_length = 255)
    photoID = models.IntegerField()


class Reviews(models.Model):
    userID = models.IntegerField()
    productID = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length = 999) # meira ? idunno


class Orders(models.Model):
    userId = models.IntegerField()
    shoppingCartID = models.IntegerField()
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    amount = models.FloatField()
    additionalInfo = models.CharField(max_length = 999, blank= True)
    address = models.CharField(max_length = 255)
    zipcode = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    country = models.CharField(max_length = 255)



class SearchHistory(models.Model):
    userID = models.IntegerField()
    keywordIDs = models.IntegerField()
    search = models.CharField(max_length = 255) #sentance
    datetime = models.DateTimeField(max_length=255)

class ShoppingChart(models.Model):
    userID = models.IntegerField()
    productIDs = models.IntegerField()
