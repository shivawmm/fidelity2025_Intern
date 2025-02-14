from django.db import models

class QuestionPaper(models.Model):
    subject = models.CharField(max_length=100)
    qno = models.IntegerField(unique=True)
    question = models.TextField()

    def __str__(self):
        return f"{self.qno}. {self.subject}"
