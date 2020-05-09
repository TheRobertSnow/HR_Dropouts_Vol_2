from django.forms import ModelForm
from django.forms import widgets
from django import forms
from CaptainConsole.models import Products, Users, Reviews, ProductImages, Profile

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
    image = forms.CharField(required=True, widget=forms.TextInput({'class': 'form-control'}))

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


class UserCreateForm(ModelForm):
    class Meta:
        model = Users
        exclude = ['id']
        widgets = {
            'nickname': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'avatar': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'admin': widgets.CheckboxInput(attrs={'class': 'form-control'}),
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
        model: Reviews
        exclude = ['id', 'user', 'product']
        CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
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
