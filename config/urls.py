from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from headless.controllers import account_controller

api = NinjaAPI()
api.add_router('posts', account_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
