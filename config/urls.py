"""config URL Configuration


"""
from django.contrib import admin
from django.urls import path
from headless import utils
from ninja import NinjaAPI
from headless.controllers import headless_controller
api = NinjaAPI()

api.add_router('headless' , headless_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),

]
