
from ninja import NinjaAPI
from django.contrib import admin
from django.urls import path
from headless.controllers import head_controller



api=NinjaAPI()
api.add_router('headless', head_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    
    
]
