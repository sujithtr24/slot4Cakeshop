from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('register/',views.register, name = "register"),
    path('logout/',views.logout, name="logout"),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart')
]