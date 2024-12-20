from django.contrib import admin #type: ignore
from django.urls import path #type: ignore
from film import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('details/', views.details, name='details'), 
    path('delete/<int:id>/', views.delete, name='delete'),
    path('about/', views.about, name='about'),
    path('_layout/', views.layout_view, name='layout'),
]
