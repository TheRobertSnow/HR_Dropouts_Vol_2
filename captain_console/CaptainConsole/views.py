from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from CaptainConsole.models import Products, ProductImages, Reviews, Profile, PreviouslyViewed, SearchHistory, ContactInfo, PaymentInfo
from CaptainConsole.forms.cc_form import ProductCreateForm, ProductUpdateForm, AddImageForm, ProfileForm, ReviewCreateForm, CustomUserCreationForm, PreviouslyViewedForm, SearchHistoryForm, ContactInfoForm, PaymentInfoForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from cart.cart import Cart

# Create your views here.
def home(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        if request.user.is_authenticated:
            form = SearchHistoryForm()
            search = form.save(commit=False)
            search.user = request.user
            search.searchQuery = search_filter
            search.datetime = timezone.now()
            search.save()
        ty = request.headers['addType']
        cat = request.headers['addCategory']
        order = request.headers['addFilter']
        products = []

        if order == 'by_name':
            productdata = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'manufacturer': x.manufacturer,
                'category': x.category,
                'description': x.description,
                'type': x.type,
                'mainImageLink': x.mainImageLink
            } for x in Products.objects.filter(name__icontains=search_filter).order_by('name')]
        elif order == 'by_price':
            productdata = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'manufacturer': x.manufacturer,
                'category': x.category,
                'description': x.description,
                'type': x.type,
                'mainImageLink': x.mainImageLink
            } for x in Products.objects.filter(name__icontains=search_filter).order_by('price')]
        else:
            productdata = [{
                'id': x.id,
                'name': x.name,
                'price': x.price,
                'manufacturer': x.manufacturer,
                'category': x.category,
                'description': x.description,
                'type': x.type,
                'mainImageLink': x.mainImageLink
            } for x in Products.objects.filter(name__icontains=search_filter)]

        for product in productdata:
            add_to_list = True
            if cat != 'none':
                if product['category'] != cat:
                    add_to_list = False
            if ty != 'none':
                if product['type'] != ty:
                    add_to_list = False
            if add_to_list:
                products.append(product)

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
    return render(request, 'CaptainConsole/create_product.html', {'form': form})

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
def search_history(request):
    userID = request.user.id
    searches = []
    for x in SearchHistory.objects.all():
        if x.user_id == userID:
            searches.append(x)
    return render(request, 'CaptainConsole/search_history.html', {'searches': searches})


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

def cart_info(request):
    return render(request, 'CaptainConsole/cart-detail.html')

def contact_info(request):
    contactinfo = ContactInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ContactInfoForm(instance=contactinfo, data=request.POST)
        if form.is_valid():
            contactinfo = form.save(commit=False)
            contactinfo.user = request.user
            contactinfo.save()
            return redirect('shipping_and_payment')
    return render(request, 'CaptainConsole/contact_info.html', {'form': ContactInfoForm(instance=contactinfo)})

def shipping_and_payment(request):
    paymentinfo = PaymentInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = PaymentInfoForm(instance=paymentinfo, data=request.POST)
        if form.is_valid():
            paymentinfo = form.save(commit=False)
            paymentinfo.user = request.user
            paymentinfo.save()
            return redirect('order_review')
    return render(request, 'CaptainConsole/shipping_and_payment.html', {'form': PaymentInfoForm(instance=paymentinfo)})

def order_review(request):
    contactinfo = ContactInfo.objects.filter(user=request.user).first()
    paymentinfo = PaymentInfo.objects.filter(user=request.user).first()
    return render(request, 'CaptainConsole/order_review.html', {
        'payment': PaymentInfoForm(instance=paymentinfo),
        'contact': ContactInfoForm(instance=contactinfo)})

@login_required
def delete_search_history(request):
    SearchHistory.objects.all().delete()
    return redirect('home')

@login_required
def delete_previously_viewed(request):
    PreviouslyViewed.objects.all().delete()
    return redirect('home')

