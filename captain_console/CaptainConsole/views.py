from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from CaptainConsole.models import Products, ProductImages, Reviews, Profile, PreviouslyViewed
from CaptainConsole.forms.cc_form import ProductCreateForm, ProductUpdateForm, AddImageForm, ProfileForm, ReviewCreateForm, CustomUserCreationForm, PreviouslyViewedForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from cart.cart import Cart

# Create your views here.
def home(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        if request.headers['addFilter'] == 'by_name':
            products = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'description': x.description,
                'mainImageLink': x.mainImageLink
            } for x in Products.objects.filter(name__icontains=search_filter).order_by('name')]
        elif request.headers['addFilter'] == 'by_price':
            products = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'description': x.description,
                'mainImageLink': x.mainImageLink
            } for x in Products.objects.filter(name__icontains=search_filter).order_by('price')]
        else:
            products = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'description': x.description,
                'mainImageLink': x.mainImageLink
            } for x in Products.objects.filter(name__icontains=search_filter)]
        return JsonResponse({ 'data': products })
    if request.user.is_authenticated:
        context = {'products': Products.objects.all(),
                   'previous': PreviouslyViewed.objects.filter(user=request.user).order_by('-datetime')[:5]}
    else:
        context = {'products': Products.objects.all()}
    return render(request, 'CaptainConsole/home.html', context)

def get_product_by_id(request, id):
    if request.user.is_authenticated:
        form = PreviouslyViewedForm()
        prod = get_object_or_404(Products, pk=id)
        prev = form.save(commit=False)
        prev.product = prod
        prev.user = request.user
        prev.datetime = timezone.now()
        prev.save()
    context = {'product': get_object_or_404(Products, pk=id), 'images': ProductImages.objects.all(),
               'reviews': Reviews.objects.all(), 'profiles': Profile.objects.all()}
    return render(request, 'CaptainConsole/product.html', context)

@login_required
def add_product(request):
    return render(request, 'CaptainConsole/create_product.html')

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductCreateForm()
    return render(request, 'CaptainConsole/create_product.html', {
        'form': form
    })

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'CaptainConsole/signup.html', {'form': form})

@login_required
def delete_product(request, id):
    product = get_object_or_404(Products, pk=id)
    product.delete()
    return redirect('home')

@login_required
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

@login_required
def add_image(request, id):
    if request.method == 'POST':
        form = AddImageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=id)
    else:
        form = AddImageForm()
    return render(request, 'CaptainConsole/add_image.html', {
        'form': form,
        'id': id
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'CaptainConsole/profile.html', {
        'form': ProfileForm(instance=profile)
    })

def review(request, id):
    review = Reviews.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ReviewCreateForm(instance=review, data=request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product_id = id
            review.datetime = timezone.now()
            review.save()
            return redirect('product_details', id=id)
    return render(request, 'CaptainConsole/review.html', {
        'form': ReviewCreateForm(instance=review)
    })

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")

@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required
def cart_detail(request):
    return render(request, 'CaptainConsole/cart-detail.html')

