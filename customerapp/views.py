from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from adminapp.models import cake_tbl

# Create your views here.
# name = "Sachin"
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        cn = request.POST['fullname']
        cm = request.POST['email']
        cp = request.POST['phone']
        cpass = request.POST['password']

        # print(cn,cm,cp,cpass)

        obj = customer_tbl.objects.create(
            customer_name = cn,
            customer_email = cm,
            customer_phone = cp,
            customer_password = cpass
        )

        if obj:
            return render(request, 'login.html')
        else:
            return render(request,'register.html')
        
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        # print(request.__dict__)

        ce = request.POST.get('email')
        cp = request.POST.get('password')

        # print(ce,cp)

        obj = customer_tbl.objects.filter(
            customer_email = ce,
            customer_password = cp
        )

        if obj:
            for i in obj:
                # print(i.__dict__)
                request.session['user_id'] = i.id
            return render(request, 'home.html')
        return render(request, 'login.html', {"error":"Invalid email or password"})

        
def logout(request):
    if request.session['user_id']:
        # del request.session['user_id'] 
        request.session.flush()
        return render(request,'home.html')
    
    else:
        return render(request,'home.html')

def products(request):
    if 'user_id' not in request.session:
        return redirect('login')
    cakes = cake_tbl.objects.all()
    return render(request, 'products.html', {'cakes': cakes})


def add_to_cart(request, cake_id):
    if 'user_id' not in request.session:
        return redirect('login')
    
    customer = customer_tbl.objects.get(id=request.session['user_id'])
    cake = cake_tbl.objects.get(id=cake_id)
    
    # Check if item already exists in the cart for this customer
    cart_item, created = cart_tbl.objects.get_or_create(customer=customer, cake=cake)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('products')

def increment_cart(request, cart_id):
    if 'user_id' not in request.session:
        return redirect('login')
    try:
        cart_item = cart_tbl.objects.get(id=cart_id, customer__id=request.session['user_id'])
        cart_item.quantity += 1
        cart_item.save()
    except cart_tbl.DoesNotExist:
        pass
    return redirect('cart')

def decrement_cart(request, cart_id):
    if 'user_id' not in request.session:
        return redirect('login')
    try:
        cart_item = cart_tbl.objects.get(id=cart_id, customer__id=request.session['user_id'])
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
    except cart_tbl.DoesNotExist:
        pass
    return redirect('cart')

def remove_cart_item(request, cart_id):
    if 'user_id' not in request.session:
        return redirect('login')
        
    try:
        cart_item = cart_tbl.objects.get(id=cart_id, customer__id=request.session['user_id'])
        cart_item.delete()
    except cart_tbl.DoesNotExist:
        pass
    return redirect('cart')
    

def cart(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    customer = customer_tbl.objects.get(id=request.session['user_id'])
    cart_obj = cart_tbl.objects.filter(customer=customer)

    grand_total = sum(item.total_amount() for item in cart_obj)
    cart_count = sum(item.quantity for item in cart_obj)
    return render(request, 'cart.html', {'cart_obj': cart_obj, "grand_total": grand_total, "cart_count": cart_count})