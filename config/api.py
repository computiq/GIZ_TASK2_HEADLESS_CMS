from ninja import NinjaAPI
from headless.api import router as posts_router

api = NinjaAPI()

api.add_router('/posts/', posts_router)