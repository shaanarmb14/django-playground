from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.logging import LoggingInstrumentor

from .models import Movie
from .serializers import MovieSerializer

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({"service.name": "crud-api"})
    )
)
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("crud_api")

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
    with tracer.start_as_current_span("get-movie-by-id"):
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)
            logger.info(f"Movie with ID {movie_id} retrieved successfully.")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            logger.error(f"Movie with ID {movie_id} not found.")
            return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

def __createMovie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def __updateMovie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

def __deleteMovie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return Response({"message": "Movie deleted."}, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)