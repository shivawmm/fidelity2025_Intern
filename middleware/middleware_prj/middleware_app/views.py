from django.shortcuts import render
from .models import Employee
from django.db.models import Sum

def get(request):
    employees = Employee.objects.filter(salary__gt=5000) 
    total_salary = employees.aggregate(total_salary=Sum('salary'))  
    
    print(total_salary)

    return render(request, 'index.html', {'employees': employees, 'total_salary': total_salary['total_salary']})
