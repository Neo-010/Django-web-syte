<<<<<<< HEAD
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('film.urls')),
    path("film/", include("film.urls")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
from django.contrib import admin #type: ignore
from django.urls import include, path #type: ignore

from film import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about),
    path("users/", include("users.urls")),
]
>>>>>>> 68cdfb849ce52235a489914a0e13f457e181b026
