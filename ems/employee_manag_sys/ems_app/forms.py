from django import forms
from .models import Employee

class EmployeeRegisterForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'date_of_joining']

class EmployeeLoginForm(forms.Form):
    employee_id = forms.CharField(max_length=10)
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'date_of_joining']