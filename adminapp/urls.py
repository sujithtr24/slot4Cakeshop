from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.adminHome, name="adminHome"),
    path('customers/',views.adminCustomers, name= 'adminCustomers'),
    path('customers/edit/<int:customer_id>/', views.adminEditCustomer, name='adminEditCustomer'),
    path('customers/delete/<int:customer_id>/', views.adminDeleteCustomer, name='adminDeleteCustomer'),
    path('products/',views.adminProducts, name='adminProducts'),
    path('add-product',views.adminAddProducts, name='adminAddProducts')
]