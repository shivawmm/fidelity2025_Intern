from django.urls import path
from .views import get_data
from .views import create_student, get_all_students, get_student_detail, update_student, delete_student
# from rest_framework.schemas import get_schema_view
# schema_view=get_schema_view(title="restapi")
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Student API",
      default_version="v1",
      description="Student version",

      terms_of_service="",
      contact=openapi.Contact(email="xyz@example.com"),
      license=openapi.License("Open"),
   ),
   public=True,
)

urlpatterns = [
    path('get/', get_data, name='get_data'),
    path('post/', create_student, name='post_data'),
    path('getall/', get_all_students, name='get_all_data'),
    path('getbyid/<int:student_id>/', get_student_detail, name='get_student_detail'),  
    path('update/<int:student_id>/', update_student, name='update_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
]
