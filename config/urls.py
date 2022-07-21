import imp
from django.contrib import admin
from django.urls import path
from headless.controllers import api
from headless.controllers import  controll_router

api.add_router('/control',controll_router)
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('api/',api.urls)
]
