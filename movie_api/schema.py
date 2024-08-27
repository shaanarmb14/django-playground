from datetime import date
from ninja import ModelSchema, Schema
from .models import Cinema, Movie, MovieCinema

class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
        fields = "__all__"

class CreateMovieSchema(ModelSchema):
    class Meta:
        model = Movie
        exclude = ['id']

class UpdateMovieSchema(Schema):
    title: str
    release_date: date
    genre: str
    runtime: int
    synopsis: str
    director: str
    rating: str

class CinemaSchema(ModelSchema):
    class Meta:
        model = Cinema
        fields = '__all__'

class MovieCinemaSchema(ModelSchema):
    class Meta:
        model = MovieCinema
        fields = '__all__'