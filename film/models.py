from django.db import models #type: ignore


# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed  = models.CharField(max_length=255)
    producers  = models.CharField(max_length=255)
    screenwriters  = models.CharField(max_length=255)
    cinematographer  = models.CharField(max_length=255)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name

        
class Film3434(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed  = models.CharField(max_length=255)
    producers  = models.CharField(max_length=255)
    screenwriters  = models.CharField(max_length=255)
    cinematographer  = models.CharField(max_length=255)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name
