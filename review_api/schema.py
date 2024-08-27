from datetime import date
from ninja import ModelSchema, Schema

from .models import Review

class ReviewSchema(ModelSchema):
    class Meta:
        model = Review
        fields = '__all__'

class CreateReviewSchema(ModelSchema):
    class Meta:
        model = Review
        exclude = ['id']

class UpdateReviewSchema(Schema):
    score: int
    comments: str
    review_date: date