from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import cake_tbl
from customerapp.models import customer_tbl

# Create your views here.
def adminHome(request):
    return render(request,'admin/admin-dashboard.html')

def adminCustomers(request):
    customers = customer_tbl.objects.all()     # SELECT * FROM users;
    return render(request,'admin/admin-customers.html',{'users':customers})
 
def adminProducts(request):
    return render(request,'admin/admin-products.html')

def adminAddProducts(request):
    if request.method == 'POST':
        cn = request.POST['cake_name']
        cp = request.POST['cake_price']
        cd = request.POST['cake_description']
        cc = request.POST['cake_category']
        ci = request.FILES['cake_image']

        obj = cake_tbl.objects.create(
            cake_name = cn,
            cake_price = cp,
            cake_description = cd, 
            cake_category = cc,
            cake_image = ci
        )
        if obj:
            return render(request,'admin/admin-addProduct.html',{"sucess":"Cake uploaded sucessfully"})
        else:
            return render(request,'admin/admin-addProduct.html',{"error":"cake not uploaded"})
    return render(request,'admin/admin-addProduct.html')

def adminEditCustomer(request, customer_id):
    customer = customer_tbl.objects.get(id=customer_id)
    if request.method == 'POST':
        # Take inputs from HTML form to single elements
        name = request.POST.get('customer_name')
        email = request.POST.get('customer_email')
        phone = request.POST.get('customer_phone')
        
        customer.customer_name = name
        customer.customer_email = email
        customer.customer_phone = phone
        
        customer.save()
        
        return redirect('adminCustomers')
    return render(request, 'admin/admin-editCustomer.html', {'customer': customer})

def adminDeleteCustomer(request, customer_id):
    customer = customer_tbl.objects.get(id=customer_id)
    customer.delete()
    return redirect('adminCustomers')

