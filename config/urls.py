from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from headless.controllers import end_points

api = NinjaAPI()
api.add_router('/methods',end_points)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',api.urls)
]
