from rest_framework import serializers
from .models import Cinema, Movie, MovieCinema

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class MovieCinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCinema
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    cinemas = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'genre', 'runtime', 'synopsis', 'director', 'rating', 'cinemas']

    def get_cinemas(self, obj):
        movie_cinemas = MovieCinema.objects.filter(movie=obj)
        return MovieCinemaSerializer(movie_cinemas, many=True).data