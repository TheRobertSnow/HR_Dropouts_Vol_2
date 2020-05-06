from django.shortcuts import render, get_object_or_404
from django.http import Http404

products = [
    {'id':'0','image':'1.jpg', 'name':'PlayStation1', 'price': 19.99, 'description':'This is some long as description of the item'},
    {'id':'1','image':'2.jpg', 'name':'PlayStation2', 'price': 19.99, 'description':'This is some long as description of the item'},
    {'id':'2','image':'3.jpg', 'name':'PlayStation3', 'price': 9.99, 'description':'This is some long as description of the item'},
    {'id':'3','image':'4.jpg', 'name':'PlayStation4', 'price': 8.99, 'description':'This is some long as description of the item'},
    {'id':'4','image':'5.jpg', 'name':'Xbox 360', 'price': 7.99, 'description':'This is some long as description of the item'},
    {'id':'5','image':'6.jpg', 'name':'Xbox One', 'price': 6.99, 'description':'This is some long as description of the item'},
    {'id':'6','image':'7.jpg', 'name':'Sega Genesis', 'price': 19.99, 'description':'This is some long as description of the item'},
    {'id':'7','image':'2.jpg', 'name':'PlayStation2', 'price': 19.99, 'description':'This is some long as description of the item'},
    {'id':'8','image':'2.jpg', 'name':'PlayStation2', 'price': 19.99, 'description':'This is some long as description of the item'},
    {'id':'9','image':'2.jpg', 'name':'PlayStation2', 'price': 19.99, 'description':'This is some long as description of the item'},
    {'id':'10','image':'2.jpg', 'name':'PlayStation2', 'price': 19.99, 'description':'This is some long as description of the item'},
]
# Create your views here.
def home(request):
    return render(request, 'CaptainConsole/home.html', context={ 'products': products })

def login(request):
    return render(request, 'CaptainConsole/login.html')

def get_product_by_id(request, id):
    return render(request, 'CaptainConsole/product.html', context={ 'product': products[id] })