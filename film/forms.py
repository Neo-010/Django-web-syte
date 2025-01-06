# film/forms.py
from django import forms #type: ignore
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
