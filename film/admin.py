from django.contrib import admin
from .models import Film

class FilmAdmin(admin.ModelAdmin):
    # Відображаємо колонки для перегляду
    list_display = ('name', 'genres', 'directed', 'year', 'poster')  
    
    # Додаємо можливість пошуку по полях
    search_fields = ('name', 'genres', 'directed')  
    
    # Додаємо фільтрацію по року
    list_filter = ('year',)

# Зареєструємо модель Film в адмін панелі
admin.site.register(Film, FilmAdmin)