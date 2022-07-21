import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse

def list_posts():
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_post(title, content):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def update_post(title, content):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_post(title):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def del_post(title):
    pass
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(f"posts/{title}.md")
        return HttpResponse(status=204)#There is no content to send for this request, but the headers may be useful
