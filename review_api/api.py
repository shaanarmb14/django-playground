from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Router, Schema, PatchDict

from core.schema import NotFoundError
from .schema import CreateReviewSchema, ReviewSchema, UpdateReviewSchema
from .models import Review

router = Router()

@router.get(
    "/", 
    summary="Get all movies",
    response={ 200: list[ReviewSchema], 204: None }
)
def index(request):
    queryset = Review.objects.all()
    if not queryset.exists():
        return HttpResponse(status=204)
    return queryset

@router.get(
    "/{review_id}",
    summary="Get a review by id",
    response={ 200: ReviewSchema, 404: NotFoundError }
)
def get_by_id(request, review_id: int):
    return get_object_or_404(Review, id=review_id)

@router.post(
    "/",
    summary="Create a new review",
    response={201: ReviewSchema}
)
def create(request, payload: CreateReviewSchema):
    return Review.objects.create(**payload.dict())

@router.patch(
    "/{review_id}", 
    summary="Update a review",
    response={ 200: ReviewSchema, 404: NotFoundError }
)
def update_movie(request, review_id: int, payload: PatchDict[UpdateReviewSchema]):
    obj = get_object_or_404(Review, id=review_id)

    for attr, value in payload.items():
        setattr(obj, attr, value)

    obj.save()

    return obj

@router.delete(
    "/{review_id}", 
    summary="Delete a review",
    response={ 200: None, 404: NotFoundError}
)
def delete_movie(request, review_id: int):
    review = get_object_or_404(Review, id=review_id);
    Review.objects.delete(review)
    return HttpResponse(status=200)