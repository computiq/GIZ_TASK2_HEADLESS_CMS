"""
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from headless.controllers import postController

api = NinjaAPI()
api.add_router('/posts',postController)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
