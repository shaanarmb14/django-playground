from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Router, Schema

from .schema import CreateMovieSchema, MovieSchema
from .models import Movie

router = Router()

class NotFoundError(Schema):
    detail: str

@router.get(
    "/", 
    summary="Get all movies",
    response={200: list[MovieSchema], 204: None}
)
def index(request):
    queryset = Movie.objects.all()
    if not queryset.exists():
        return HttpResponse(status=204)
    return queryset

@router.post(
    "/",
    summary="Create a new movie",
    response={201: MovieSchema}
)
def create(request, data: CreateMovieSchema):
    print("Debug - movie data:", data.dict())
    return Movie.objects.create(**data.dict())

@router.get("/{movie_id}", response={200: MovieSchema, 404: NotFoundError})
def get_by_id(request, movie_id: int):
    return get_object_or_404(Movie, id=movie_id)

# @router.delete("/{movie_id}")
# def get_by_id(request, movie_id: int):
#     return __deleteMovie(request, movie_id)

# @router.patch("/{movie_id}")
# def update_movie(request, movie_id):
#         return __updateMovie(request, movie_id)
    