<<<<<<< HEAD
# film/forms.py
from django import forms #type: ignore
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
=======
from django import forms #type: ignore
from film.models import Film


class CreateFilm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026
