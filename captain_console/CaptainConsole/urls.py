from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login', LoginView.as_view(template_name='CaptainConsole/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('sign_up', views.create_user, name='sign_up'),
    path('products/<int:id>', views.get_product_by_id, name='product_details'),
    path('create_product', views.create_product, name='create_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('product_img/<int:id>', views.add_image, name='add_image'),
    path('profile', views.profile, name='profile'),
    path('product/<int:id>/review', views.review, name='review_product'),
]
