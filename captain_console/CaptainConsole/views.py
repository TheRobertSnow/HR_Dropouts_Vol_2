from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from CaptainConsole.models import Products, ProductImages
from CaptainConsole.forms.cc_form import ProductCreateForm, ProductUpdateForm

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
    context = {'products': Products.objects.all().order_by('name')}
    return render(request, 'CaptainConsole/home.html', context)

def login(request):
    return render(request, 'CaptainConsole/login.html')

def get_product_by_id(request, id):
    return render(request, 'CaptainConsole/product.html', {
        'product': get_object_or_404(Products, pk=id)
    })

def add_product(request):
    return render(request, 'CaptainConsole/create_product.html')

def sign_up(request):
    return render(request, 'CaptainConsole/signup.html')

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

def delete_product(request, id):
    product = get_object_or_404(Products, pk=id)
    product.delete()
    return redirect('home')

def update_product(request, id):
    instance = get_object_or_404(Products, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request, 'CaptainConsole/update_product.html', {
        'form': form,
        'id': id
    })