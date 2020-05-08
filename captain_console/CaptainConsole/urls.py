from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('products/<int:id>', views.get_product_by_id, name='product_details'),
    path('create_product', views.create_product, name='create_product'),
    path('sign_up', views.sign_up, name='sign_up'),
]
