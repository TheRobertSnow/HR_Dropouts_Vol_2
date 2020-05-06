from django.shortcuts import render
products = [
    {'name':'PlayStation2', 'price': 19.99},
    {'name':'wii', 'price': 3.99},
    {'name':'Xbox360', 'price': 5.99},
    {'name':'He on xgames', 'price': 8.49},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
    {'name':'wii', 'price': 3.99},
]
# Create your views here.
def home(request):
    return render(request, 'CaptainConsole/home.html', context={ 'products': products })

def login(request):
    return render(request, 'CaptainConsole/login.html')
