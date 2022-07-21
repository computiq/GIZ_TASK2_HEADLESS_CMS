import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from ninja import Router
from headless.utils import * 

post_controller = Router()

@post_controller.get("/")
def List(request):
    return list_posts()

@post_controller.get("/Title")
def Git_Title(request,title):
    return get_post(title)


@post_controller.post("/Post")
def Post(request, title,content):
    return save_post(title,content)

@post_controller.put("/Put")
def Update(request, title,content):
    return save_post(title,content)

@post_controller.delete("Delet")
def Delete(request,title):
    return del_post(title)