from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, StockForm
from .models import Stock
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def home(request):
    stocks = Stock.objects.filter(user=request.user)
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = request.user
            stock.save()
    else:
        form = StockForm()
    return render(request, 'home.html', {'stocks': stocks, 'form': form})

@login_required
def update_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id, user=request.user)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StockForm(instance=stock)
    return render(request, 'update_stock.html', {'form': form})

@login_required
def delete_stock(request, stock_id):
    stock = Stock.objects.get(id=stock_id, user=request.user)
    stock.delete()
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('welcome')

def welcome(request):
    return render(request, 'welcome.html')