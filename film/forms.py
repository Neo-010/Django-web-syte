from django import forms #type: ignore
from film.models import Film


class CreateFilm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
