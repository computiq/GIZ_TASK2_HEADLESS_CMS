import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files import File

def list_posts():
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

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


def update_funct(title, old_content ,new_content): 
    filename = f"posts/{title}.md"
    with open(filename, 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(old_content, new_content)
    with open(filename, 'w') as file:
        file.write(filedata)

    


def del_post(title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)