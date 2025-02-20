from django.contrib import admin
from .views import get
from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get)
]