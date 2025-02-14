from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionPaperViewSet

router = DefaultRouter()
router.register(r'questionpapers', QuestionPaperViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
