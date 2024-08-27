from ninja import ModelSchema
from .models import Cinema, Movie, MovieCinema

class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
        fields = "__all__"

class CreateMovieSchema(ModelSchema):
    class Meta:
        model = Movie
        exclude = ['id']

class CinemaSchema(ModelSchema):
    class Meta:
        model = Cinema
        fields = '__all__'

class MovieCinemaSchema(ModelSchema):
    class Meta:
        model = MovieCinema
        fields = '__all__'