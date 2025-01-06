from django.db import models #type: ignore

class Film(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed = models.CharField(max_length=255)
    producers = models.CharField(max_length=255)
    screenwriters = models.CharField(max_length=255)
    cinematographer = models.CharField(max_length=255)
    year = models.IntegerField()
    #image = models.ImageField(upload_to='films/images/', blank=True, null=True)

    def __str__(self):
        return self.name
