from django.db import models

# Create your models here.

class Parents(models.Model):
     
     type = models.CharField(max_length=50)
     name = models.CharField(max_length=60)
     last_name = models.CharField(max_length=60)
     age = models.IntegerField()
     birth = models.DateField()

