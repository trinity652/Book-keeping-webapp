from django.db import models

# Create your models here.
class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    title = models.CharField(max_length=200)
    Id = models.CharField(max_length=12,primary_key=True)
    publisher = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    copies=models.IntegerField()