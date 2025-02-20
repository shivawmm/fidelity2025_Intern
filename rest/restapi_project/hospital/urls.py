from django.urls import path
from .views import PatientCreateView, PatientListView, PatientDetailView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
]
