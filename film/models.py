from django.db import models #type: ignore

class Film(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    directed = models.CharField(max_length=255)
    year = models.IntegerField()
    poster = models.ImageField(upload_to='images/', blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    