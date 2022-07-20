import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Router
import json
from .utils import save_post, get_post


api = NinjaAPI()
headless = Router()


@api.get("/posts")
def list_posts(request):
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

@api.post("posts/{title}/{content}")
def save_post(request, title,content):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


@api.get("posts/{title}")
def get_post(request, title):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None.
    """
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


@api.delete("posts/{title}")
def del_post(request, title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
