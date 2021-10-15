import os
from ninja import Router ,Schema
import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


headless_controller = Router()


@headless_controller.get('')
def list_Posts(request):
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
    
    
    


@headless_controller.get('{title}')
def get_post(request,title):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


@headless_controller.post('')
def save_post(request,title, content):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))




@headless_controller.put('{title}')
def update_post(request,title, content):
    try:
        filename = f"posts/{title}.md"
        my_file = open(filename, "w")
        my_file.write(content)  # or we can use append for just adding
        my_file.close()
    except FileNotFoundError:
        return None


@headless_controller.put('{titl}')
def append_post(request,titl, content):
    try:
        filename = f"posts/{titl}.md"
        with open(filename, "a") as myfile:
            myfile.write("appended text")
    except FileNotFoundError:
        return None

@headless_controller.delete('{title}')
def del_post(request,title):
    try:
        filename = f"posts/{title}.md"
        if default_storage.exists(filename):
            default_storage.delete(filename)          # or we can use return os.remove(f"posts/{title}.md")
    except FileNotFoundError:
        return None






