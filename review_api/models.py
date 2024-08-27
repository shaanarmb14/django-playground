from django.db import models

from core.base_models import TimeStampedModel

# Create your models here.
class Review(TimeStampedModel):
    movie = models.ForeignKey(
        'movie_api.Movie', 
        on_delete=models.CASCADE,
        related_name='reviews')
    score = models.DecimalField(max_digits=4, decimal_places=2)
    comments = models.TextField()
    review_date = models.DateTimeField()