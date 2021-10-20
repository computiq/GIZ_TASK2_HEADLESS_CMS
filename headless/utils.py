import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_posts():
    "Returns list for all blog names"
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_post(title, content):
    "This function saves a blog post based on its title and content.If a post with the identical title already exists, it will be replaced"
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_post(title):
    "Returns a post based on its title. If there is no such post, the function returns None"
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def del_post(title):
    " Removes a post based on its title. If there is no such post, the function returns None"
    try:
        path = (f"posts/{title}.md")
        file_content = default_storage.open(path).read().decode("utf-8")
        default_storage.delete(path)
        return file_content
    except FileNotFoundError:
        return None