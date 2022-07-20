from ninja import NinjaAPI
import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from . import utils

api = NinjaAPI()


@api.post("create")
def save_post(request, title, content):
    utils.save_post(title, content)


@api.get("get")
def list_posts(request):
    return {'posts': utils.list_posts()}


@api.get("get_title")
def get_post(request, title):
    return {'post': utils.get_post(title)}


@api.put("get")
def update_post(request, title, content):
    utils.save_post(title, content)


@api.delete("get title")
def delete_post(request, title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.delete(filename)
