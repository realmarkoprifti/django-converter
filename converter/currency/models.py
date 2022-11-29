from django.db import models

# Create your models here.

class Coin(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=70)
    symbol = models.CharField(max_length=5, blank=True)
    
    def __str__(self):
        return f"{self.id}, {self.name}"