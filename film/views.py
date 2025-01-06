from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
<<<<<<< HEAD
from django.urls import reverse # type: ignore
from .forms import FilmForm
from film.models import Film

def home(request):
    films = Film.objects.all() 
    return render(request, 'film/film_list.html', {'films': films})

def create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)  
        if form.is_valid():
            film = form.save()  # зберігаємо
            print(f"Film created: {film}")  # перевірка в консолі
            return redirect('home')  # виконуємо редірект на home
        else:
            print(form.errors)  # якщо є помилки
    else:
        form = FilmForm()
    return render(request, 'film/create.html', {'form': form})
=======




from film.forms import CreateFilm
from film.models import Film

def home(request):
    film = Film.objects.all()
    return render(request, "index.html", {"films": film})


def create(request):
    form = CreateFilm()

    if request.method == "POST":
        form = CreateFilm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/films/home")

    return render(request, "create.html", {"form": form})

>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026

def details(request, id):
    film = Film.objects.get(id=id)

    return render(request, "details.html", {"film": film})


<<<<<<< HEAD

def delete_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == "POST":
        film.delete()
        return redirect('home')
    return render(request, 'delete_film.html', {'film': film})


def view_film(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'view_film.html', {'film': film})

def about(request):
    return HttpResponse("<h1>About Page!</h1>")

def layout_view(request):
    return render(request, '_layout.html')
=======
def delete(request, id):
    film = get_object_or_404(Film, id=id)
    film.delete()
    return redirect("/films/home")


def about(request):
    return HttpResponse("<h1>About Page!</h1>")
>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026
