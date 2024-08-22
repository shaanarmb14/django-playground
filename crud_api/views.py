from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie
from .serializers import MovieDetailSerializer, MovieSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return __getMovies(request)
    elif request.method == 'POST':
        return __createMovie(request)

@api_view(['GET', 'DELETE', 'PATCH'])
def movie_by_id_handler(request, movie_id):
    if request.method == 'GET':
        return __getMovieByID(request, movie_id)
    elif request.method == 'DELETE':
        return __deleteMovie(request, movie_id)
    elif request.method == 'PATCH':
        return __updateMovie(request, movie_id)
    
def __getMovies(request):
    queryset = Movie.objects.all()
    title = request.query_params.get('title')
    genre = request.query_params.get('genre')

    if title is not None:
        queryset = queryset.filter(title=title)
    if genre is not None:
        queryset = queryset.filter(genre=genre)

    serializer = MovieSerializer(queryset, many=True)
    return Response(serializer.data)

def __getMovieByID(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

def __createMovie(request):
    serializer = MovieSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def __updateMovie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie, data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

def __deleteMovie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return Response({"message": "Movie deleted."}, status=status.HTTP_200_OK)