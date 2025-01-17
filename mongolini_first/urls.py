from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from film import views 

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # Адмін-панель
    path('', views.home, name='home'),  # Головна сторінка
    path('film/', include('film.urls')),  # Підключення URL-патернів з додатку "film"
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)