from django.db import models

class Product(models.Model):
    pid = models.CharField(max_length=10, unique=True, primary_key=True)
    pname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.pname