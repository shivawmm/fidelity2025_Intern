# filepath: /C:/Users/Shivam Singh/OneDrive/Desktop/Fidelity/ems/employee_manag_sys/session_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession),
    path('get/', views.getsession),

]