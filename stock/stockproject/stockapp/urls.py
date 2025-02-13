from django.urls import path
from .views import register, login_view, home, update_stock, delete_stock, logout_view, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('update_stock/<int:stock_id>/', update_stock, name='update_stock'),
    path('delete_stock/<int:stock_id>/', delete_stock, name='delete_stock'),
    path('logout/', logout_view, name='logout'),
]
