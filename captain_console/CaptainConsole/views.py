from django.shortcuts import render
products = [
    {'name':'PlayStation2', 'price': 19.99},
    {'name':'wii', 'price': 3.99},
]
# Create your views here.
def home(request):
    return render(request, 'CaptainConsole/home.html', context={ 'products': products })

def login(request):
    return render(request, 'CaptainConsole/login.html')
