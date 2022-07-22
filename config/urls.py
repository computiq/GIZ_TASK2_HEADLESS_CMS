from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from headless.utils import router


api = NinjaAPI()

api.add_router("/posts", router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
