from ninja import NinjaAPI

from crud_api.api import router as movie_router

api = NinjaAPI(
    version='1.0.0',
    title="Movies API",
    description="This is a demo API with dynamic OpenAPI info section"
)

api.add_router("/movies", movie_router, tags=["Movies"])  