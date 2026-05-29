from django.shortcuts import render, redirect
from django.http import HttpResponse
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

def cart(request):
    if 'user_id' not in request.session:
        return redirect('login')
    return render(request, 'cart.html')