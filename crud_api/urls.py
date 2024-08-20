from django.urls import path
from . import views

urlpatterns = [
    path('movies/',views.index,name='index'), # GET many, POST
    path('movies/<int:movie_id>/', views.movie_by_id_handler, name='movie'), # Get by ID
]