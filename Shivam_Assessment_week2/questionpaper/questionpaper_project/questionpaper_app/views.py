from rest_framework import viewsets
from .models import QuestionPaper
from .serializers import QuestionPaperSerializer

class QuestionPaperViewSet(viewsets.ModelViewSet):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer
