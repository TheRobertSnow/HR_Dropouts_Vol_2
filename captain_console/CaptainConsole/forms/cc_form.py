from django.forms import ModelForm
from django.forms import widgets
from django.forms import DateTimeField
from django import forms
from CaptainConsole.models import Products, Reviews, ProductImages, Profile

class ProductUpdateForm(ModelForm):

    class Meta:
        model = Products
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.TextInput(attrs={'class': 'form-control'}),
            'mainImage': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class ProductCreateForm(ModelForm):
    class Meta:
        model = Products
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.TextInput(attrs={'class': 'form-control'}),
            'mainImage': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class AddImageForm(ModelForm):
    class Meta:
        model = ProductImages
        exclude = ['id']
        widgets = {
            'imageFileName': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class ReviewCreateForm(ModelForm):
    class Meta:
        model = Reviews
        exclude = ['id', 'user', 'product', 'datetime']
        CHOICES = ((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars'),)
        widgets = {
            'rating': widgets.Select(attrs={'class': 'form-control'}, choices=CHOICES),
            'reviewTitle': widgets.TextInput(attrs={'class': 'form-control'}),
            'reviewText': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'id', 'user']
        widgets = {
            'nickname': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }
