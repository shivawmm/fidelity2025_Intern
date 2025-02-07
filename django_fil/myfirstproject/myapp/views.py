from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
def index(request):
    return HttpResponse("Hello from my app")

def form(request):
    print(request.POST)
    return render(request, 'form.html')

def contactapp(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, email, message)
    else:
        form = ContactForm()
    # print(request.POST)
    return render(request, 'contactapp.html', {'contactapp': form})

# Create your views here.
