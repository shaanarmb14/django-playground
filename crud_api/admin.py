from django.contrib import admin

from .models import Cinema, Movie, MovieCinema

# Register your models here.
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(MovieCinema)