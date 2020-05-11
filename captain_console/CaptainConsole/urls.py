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
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
    path('order/cart_info/', views.cart_info, name='cart_info'),
    path('order/contact_info/', views.contact_info, name='contact_info'),
    path('order/shipping_and_payment/', views.shipping_and_payment, name='shipping_and_payment'),
    path('order/order_review/', views.order_review, name='order_review'),
]
