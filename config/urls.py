from django.contrib import admin
from django.urls import path
from headless.controllers import router as headlessRouter
from ninja import NinjaAPI

api = NinjaAPI()

api.add_router('',headlessRouter)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',api.urls)
]
