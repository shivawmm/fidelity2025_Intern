from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from viewset_app.views import PatientViewSet
routers = routers.DefaultRouter()
routers.register('patient', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(routers.urls))
]