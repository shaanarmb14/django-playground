from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

@extend_schema(
    tags=['Reviews'],
    methods=['GET'],
)
@extend_schema(
    tags=['Reviews'],
    methods=['POST'],
)
@api_view(['GET', 'POST'])
def index(request):
    return Response({"message": f"Review {request.method} API"}, status=status.HTTP_200_OK)
