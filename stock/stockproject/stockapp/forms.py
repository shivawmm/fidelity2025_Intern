from django import forms
from django.contrib.auth.models import User
from .models import Stock

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'price']
