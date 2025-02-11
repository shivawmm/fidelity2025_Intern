from django.shortcuts import redirect, render
from django.http import HttpResponse
from crud_app.forms import OrdersForm
from crud_app.models import Orders
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def orderformview(request):
    form = OrdersForm()
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Saved')
    return render(request, 'order.html', {'order': form})

def showorder(request):
    orders = Orders.objects.all()
    return render(request, 'showorder.html', {'ord': orders})

def updateorder(request, id):
    order = Orders.objects.get(ordId=id)
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        form = OrdersForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponse('Data Updated')
    return render(request, 'order.html', {'order': form})

def deleteorder(request, id):
    order = Orders.objects.get(ordId=id)
    order.delete()
    return redirect('/show/')

def setsession(request):
    request.session['name'] = 'Steve'
    return HttpResponse('Session Set')

def getsession(request):
    name = request.session['name']
    return HttpResponse(name)

def showstatic(request):
    return render(request, 'staticfile.html')
    
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('/api/order/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, password=password1, email=email)
        user.is_active = True 
        user.save()
        messages.success(request, 'Account created successfully! Please wait for admin approval.')
        return redirect('/api/login/')
    return render(request, 'signup.html')