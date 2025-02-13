from django.shortcuts import redirect, render
from django.http import HttpResponse
from ems_app.models import Employee
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("a")
            return redirect('/api/order/')
        else:
            print("b")
            messages.error(request, 'Invalid username or password')
    print("c")    
    return render(request, 'login.html', )

@login_required
def orderformview(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        print("e")
        return redirect('login')
    employee = Employee.objects.get(employee_id=employee_id)
    return render(request, 'order.html', {'employee': employee})
