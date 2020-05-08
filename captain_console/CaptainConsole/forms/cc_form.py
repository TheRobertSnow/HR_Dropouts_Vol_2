from django.forms import ModelForm
from django.forms import widgets
from django import forms
from CaptainConsole.models import Products


class ProductCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput({'class': 'form-control'}))

    class Meta:
        model = Products
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control' }),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': widgets.TextInput(attrs={'class': 'form-control'}),
        }