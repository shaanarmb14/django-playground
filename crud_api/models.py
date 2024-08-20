from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    release_date = models.DateField()
    genre = models.CharField(max_length=64)
    runtime = models.IntegerField()
    synopsis = models.TextField()
    director = models.CharField(max_length=64)
    rating = models.CharField(max_length=8)
    princess_movie_theatre_id = models.CharField(max_length=16)

class Cinema(models.Model):
    name = models.CharField(max_length=64)
    location = models.TextField()

class MovieCinema(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)  
    showtime = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=4, decimal_places=2)