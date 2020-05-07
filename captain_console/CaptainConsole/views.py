from django.shortcuts import render, get_object_or_404
from django.http import Http404
from CaptainConsole.models import Products
from CaptainConsole.models import ProductImages

# Create your views here.
def home(request):
    context = {'products': Products.objects.all(), 'images': ProductImages.objects.all()}
    return render(request, 'CaptainConsole/home.html', context)

def login(request):
    return render(request, 'CaptainConsole/login.html')

def get_product_by_id(request, id):
    context = {'product': get_object_or_404(Products, pk=id), 'images': ProductImages.objects.all()}
    return render(request, 'CaptainConsole/product.html', context)

def add_product(request):
    return render(request, 'CaptainConsole/add_product.html')

def sign_up(request):
    return render(request, 'CaptainConsole/signup.html')
