from django.db import models

# Create your models here.
class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    publisher = models.ForeignKey('Publisher')
    author = models.ForeignKey('Author')