from django.db import models

# Create your models here.
class Users(models.Model):
    ID = models.IntegerField()
    password = models.CharField(max_length = 255) # passa hash
    avatar = models.IntegerField() # pic within the database ?? idunno
    nickname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    # admin = models.IntegerField(max_length = 255)
    admin = models.BooleanField(max_length= 255)


class Products(models.Model):
    ID = models.IntegerField()
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    description = models.CharField(max_length = 999)
    manufacturer = models.CharField(max_length = 255)
    photoID = models.IntegerField()


class Reviews(models.Model):
    ID = models.IntegerField()
    userID = models.IntegerField()
    productID = models.IntegerField()
    rating = models.IntegerField()
    review = models.CharField(max_length = 999) # meira ? idunno


class Orders(models.Model):
    ID = models.IntegerField()
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
    ID = models.IntegerField()
    userID = models.IntegerField()
    keywordIDs = models.IntegerField()
    search = models.CharField(max_length = 255) #sentance
    datetime = models.DateTimeField(max_length=255)

class ShoppingChart(models.Model):
    ID = models.IntegerField()
    userID = models.IntegerField()
    productIDs = models.IntegerField()
