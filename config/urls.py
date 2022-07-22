from django.contrib import admin
from django.urls import path
from headless.controllers import Management_Control
from ninja import NinjaAPI

api = NinjaAPI(title='Rings are cool man', description='I insist')
api.add_router("", Management_Control)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
