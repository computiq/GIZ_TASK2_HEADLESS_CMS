from ninja import Router


config_controller = Router()

import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

@config_controller.get("posts")
def list_posts(request):
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
               for filename in filenames if filename.endswith(".md")))



@config_controller.get("title")
def get_post(request, title):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


@config_controller.post("post")
def update_post(request, title, content):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


