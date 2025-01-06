from django.db import models #type: ignore

<<<<<<< HEAD
class Film(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed = models.CharField(max_length=255)
    producers = models.CharField(max_length=255)
    screenwriters = models.CharField(max_length=255)
    cinematographer = models.CharField(max_length=255)
    year = models.IntegerField()
    image = models.ImageField(upload_to='films/images/', blank=True, null=True)

    def __str__(self):
        return self.name
=======

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed  = models.CharField(max_length=255)
    producers  = models.CharField(max_length=255)
    screenwriters  = models.CharField(max_length=255)
    cinematographer  = models.CharField(max_length=255)
    year = models.IntegerField
    
    def __str__(self):
        return self.name
>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026
