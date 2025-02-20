from django.contrib import admin
from .models import Employee

admin.site.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'salary', 'date_of_joining')
    search_fields = ('firstname', 'lastname')
    list_filter = ('date_of_joining',)


