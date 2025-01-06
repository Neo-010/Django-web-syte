from django.contrib import admin #type: ignore
from django.urls import path #type: ignore
<<<<<<< HEAD
from django.conf import settings #type: ignore
from django.conf.urls.static import static  #type: ignore

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('view/<int:pk>/', views.view_film, name='view_film'),
    path('delete/<int:pk>/', views.delete_film, name='delete'),
    path('about/', views.about, name='about'),
    path('_layout/', views.layout_view, name='layout'),
]

# Додаємо обробку медіафайлів
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from film import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('details/<int:id>/', views.details, name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('about/', views.about, name='about'),
]
>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026
