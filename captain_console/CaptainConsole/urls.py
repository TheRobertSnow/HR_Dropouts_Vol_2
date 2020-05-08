from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('products/<int:id>', views.get_product_by_id, name='product_details'),
    path('create_product', views.create_product, name='create_product'),
    path('sign_up', views.create_user, name='sign_up'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('product_img/<int:id>', views.add_image, name='add_image'),
]
