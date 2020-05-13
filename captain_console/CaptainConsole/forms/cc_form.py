from django.forms import ModelForm
from django.forms import widgets
from django import forms
from CaptainConsole.models import Products, Reviews, ProductImages, Profile, PreviouslyViewed, SearchHistory, ContactInfo, PaymentInfo
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ProductUpdateForm(ModelForm):
    class Meta:
        model = Products
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.TextInput(attrs={'class': 'form-control'}),
            'mainImageLink': widgets.TextInput(attrs={'class': 'form-control'}),
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
            'category': widgets.TextInput(attrs={'class': 'from-control'}),
            'mainImageLink': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class AddImageForm(ModelForm):
    class Meta:
        model = ProductImages
        exclude = ['id', 'product']
        widgets = {
            'imageLink': widgets.TextInput(attrs={'class': 'form-control'}),
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

class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ['user']
        fields = {'fullname', 'email', 'phone', 'address', 'city', 'zip', 'country'}

class PaymentInfoForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ['user']
        fields = {'nameoncard', 'creditcardnumber', 'expirationdate', 'cvv'}

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class PreviouslyViewedForm(ModelForm):
    class Meta:
        model = PreviouslyViewed
        exclude = ['id', 'product', 'user', 'datetime']


class SearchHistoryForm(ModelForm):
    class Meta:
        model = SearchHistory
        exclude = ['id', 'user', 'searchQuery', 'datetime']