

from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True, default='0000000000', primary_key=True)
    name = models.CharField(max_length=100, default='Anonymous')
    password = models.CharField(max_length=100, default='password')
    email = models.EmailField(default='example@example.com')
    date_of_joining = models.DateField(default='2021-01-01')

    def __str__(self):
        return self.user.username