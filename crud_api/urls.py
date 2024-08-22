from django.urls import path
from . import views

urlpatterns = [
    # GET many, POST
    path('movies/',views.index,name='index'), 
    # Get, Delete, Patch by ID
    path('movies/<int:movie_id>/', views.movie_by_id_handler, name='movie'), 
]