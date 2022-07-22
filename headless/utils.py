import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_posts():
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_post(title, content):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_post(title):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None.
    """
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def del_post(title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)