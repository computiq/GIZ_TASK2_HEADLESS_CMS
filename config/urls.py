"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
#from Profile.controllors.profile_controller import profile_controller
#from account.views import auth_controller
from headless.controllers import blog_controller
api = NinjaAPI(
    version='1.0.0',
    title='Blog API v1',
    description='API documentation',

)
#api.add_router('auth', auth_controller)

api.add_router('blog_controller',blog_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),

]
