from django.contrib import admin
from django.urls import path
from headless.controllers import api
from headless.controllers import test


api.add_router('/' , test)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    
]
