from django.urls import path
from . import views
urlpatterns = [
    path('order/', views.orderformview),
    path('show/', views.showorder),
    path('update/<int:id>/', views.updateorder,name='ui'),
    path('delete/<int:id>/', views.deleteorder,name='di'),
    path('setsession/', views.setsession),
    path('getsession/', views.getsession),
    path('static/', views.showstatic),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),

]