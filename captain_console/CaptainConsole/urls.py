from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('add_product', views.add_product, name='add_product'),
    path('sign_up', views.sign_up, name='sign_up'),
]
