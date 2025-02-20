from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.id} {self.firstname} {self.lastname} {self.salary} {self.date_of_joining}"
