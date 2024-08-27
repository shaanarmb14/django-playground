from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Router, Schema, PatchDict

from core.schema import NotFoundError
from .schema import CreateMovieSchema, MovieSchema, UpdateMovieSchema
from .models import Movie

router = Router()

@router.get(
    "/", 
    summary="Get all movies",
    response={ 200: list[MovieSchema], 204: None }
)
def index(request):
    queryset = Movie.objects.all()
    if not queryset.exists():
        return HttpResponse(status=204)
    return queryset

@router.get(
    "/{movie_id}",
    summary="Get a movie by id",
    response={ 200: MovieSchema, 404: NotFoundError }
)
def get_by_id(request, movie_id: int):
    return get_object_or_404(Movie, id=movie_id)

@router.post(
    "/",
    summary="Create a new movie",
    response={201: MovieSchema}
)
def create(request, payload: CreateMovieSchema):
    print("Debug - movie data:", payload.dict())
    return Movie.objects.create(**payload.dict())

@router.patch(
    "/{movie_id}", 
    summary="Update a movie",
    response={ 200: MovieSchema, 404: NotFoundError }
)
def update_movie(request, movie_id: int, payload: PatchDict[UpdateMovieSchema]):
    obj = get_object_or_404(Movie, id=movie_id)

    for attr, value in payload.items():
        setattr(obj, attr, value)

    obj.save()

    return obj

@router.delete(
    "/{movie_id}", 
    summary="Delete a movie",
    response={ 201: None, 404: NotFoundError}
)
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id);
    Movie.objects.delete(movie)
    return HttpResponse(status=201)

    