from django.contrib import admin #type: ignore
from django.urls import path #type: ignore
from django.conf import settings #type: ignore
from django.conf.urls.static import static  #type: ignore
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),  # Список фільмів
    path('create/', views.create, name='create'),  # Створення фільму
    path('view/<int:pk>/', views.view_film, name='view_film'),  # Перегляд фільму
    path('delete/<int:pk>/', views.delete, name='delete'),  # Видалення фільму
    path('about/', views.about, name='about'),  # Про проект
    path('_layout/', views.layout_view, name='layout'),  # Загальний макет
]

# Додаємо обробку медіафайлів
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
