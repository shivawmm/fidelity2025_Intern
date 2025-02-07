from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index),
    path('form/', views.form),
    path('contactapp/', views.contactapp),
]