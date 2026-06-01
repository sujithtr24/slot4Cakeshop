from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('register/',views.register, name = "register"),
    path('logout/',views.logout, name="logout"),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('addto-cart/<int:cake_id>/', views.add_to_cart, name='addto-cart'),
    path('increment-cart/<int:cart_id>/', views.increment_cart, name='increment-cart'),
    path('decrement-cart/<int:cart_id>/', views.decrement_cart, name='decrement-cart'),
    path('remove-cart-item/<int:cart_id>/', views.remove_cart_item, name='remove-cart-item'),
]