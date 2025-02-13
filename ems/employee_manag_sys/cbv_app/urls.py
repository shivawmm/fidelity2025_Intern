from django.http import HttpResponse
from cbv_app.views import Myclass, ProductCreate, ProductUpdate, ProductList, ProductDelete
from django.urls import path

app_name='cbv_app'

urlpatterns = [
    path('cbv/', Myclass.as_view(), name='class'),
    path('create/', ProductCreate.as_view(), name = 'cbv_create'),
    path('success/', lambda request: HttpResponse('Product added successfully'), name = 'success'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name = 'cbv_update'),
    path('list/', ProductList.as_view(), name = 'product_list'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name = 'product_delete'),
]