
from sys import api_version
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from headless.controllers import headless_controller

api=NinjaAPI
api.add_router('', headless_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),  
     
]
