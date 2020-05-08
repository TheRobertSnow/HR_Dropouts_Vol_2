from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from CaptainConsole.models import Products, ProductImages, Users
from CaptainConsole.forms.cc_form import ProductCreateForm, UserCreateForm

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
    return render(request, 'CaptainConsole/create_product.html')



def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImages(imageFileName=request.POST['image'], product=product)
            product_image.save()
            return redirect('home')
    else:
        form = ProductCreateForm()
    return render(request, 'CaptainConsole/create_product.html', {
        'form': form
    })


def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'CaptainConsole/signup.html', {
        'form': form
    })



def delete_product(request, id):
    product = get_object_or_404(Products, pk=id)
    product.delete()
    return redirect('home')