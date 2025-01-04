from django.contrib import admin #type: ignore
from django.urls import include, path #type: ignore

from film import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", views.about),
    path("users/", include("users.urls")),
]
