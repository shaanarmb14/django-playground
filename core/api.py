from ninja import NinjaAPI

from movie_api.api import router as movie_router
from review_api.api import router as review_router

api = NinjaAPI(
    version='1.0.0',
    title="Playground API",
)

api.add_router("/movies", movie_router, tags=["Movies"])  
api.add_router("/reviews", review_router, tags=["Reviews"])   