from django.shortcuts import render
products = [
    {'image':'1.jpg', 'name':'PlayStation1', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'3.jpg', 'name':'PlayStation3', 'price': 9.99},
    {'image':'4.jpg', 'name':'PlayStation4', 'price': 8.99},
    {'image':'5.jpg', 'name':'Xbox 360', 'price': 7.99},
    {'image':'6.jpg', 'name':'Xbox One', 'price': 6.99},
    {'image':'7.jpg', 'name':'Sega Genesis', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
    {'image':'2.jpg', 'name':'PlayStation2', 'price': 19.99},
]
# Create your views here.
def home(request):
    return render(request, 'CaptainConsole/home.html', context={ 'products': products })

def login(request):
    return render(request, 'CaptainConsole/login.html')

def add_product(request):
    return render(request, 'CaptainConsole/add_product.html')

def sign_up(request):
    return render(request, 'CaptainConsole/signup.html')
