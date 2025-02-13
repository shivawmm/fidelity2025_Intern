from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from cbv_app.forms import ProductForm
from cbv_app.models import Product

class Myclass(View):
    def get(self, request):
        return HttpResponse('Views from class')

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'cbv_app/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return HttpResponse('Product added successfully')

    def get_success_url(self):
        return reverse_lazy('cbv_app:cbv_update', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'cbv_app/create.html'
    success_url = reverse_lazy('cbv_app:success')
    def get_success_url(self):
        return reverse_lazy('cbv_app:cbv_update', kwargs={'pk': self.object.pk})
    
class ProductList(ListView):
    model = Product
    template_name = 'cbv_app/product_list.html'
    context_object_name = 'products'

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('cbv_app:product_list')
    template_name = 'cbv_app/create.html'

