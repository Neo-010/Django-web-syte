from django.http import HttpResponse # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore




from film.forms import CreateFilm
from film.models import Film

def home(request):
    film = Film.objects.all()
    return render(request, "index.html", {"films": film})


def create(request):
    form = CreateFilm()

    if request.method == "POST":
        form = CreateFilm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/films/home")

    return render(request, "create.html", {"form": form})


def details(request, id):
    film = Film.objects.get(id=id)

    return render(request, "details.html", {"film": film})


def delete(request, id):
    film = get_object_or_404(Film, id=id)
    film.delete()
    return redirect("/films/home")


def about(request):
    return HttpResponse("<h1>About Page!</h1>")

def layout_view(request):
    return render(request, '_layout.html')
