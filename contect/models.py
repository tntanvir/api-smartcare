from django.db import models

# Create your models here.
class Contect(models.Model):
    name = models.CharField(max_length=100)
    phone= models.CharField(max_length=12)
    problems=models.TextField()

    def __str__(self):
        return f'{self.name}'