import re
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_posts():
    """
    Returns a list of all names of blog posts.
    """

    try:
        _, filenames = default_storage.listdir("posts")
        f=list(sorted(re.sub(r"\.md$", "", filename)
                            for filename in filenames if filename.endswith(".md")))
        return {"True":f}
    except  DoNotFileFound:
        return {"False":"Posts don't any found exists failed"}


def save_post(title, content):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    f=default_storage.save(filename, ContentFile(content))
    return {"True":" Create  post successfully"}

def get_post(title):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None.
    """
    if default_storage.exists(f"posts/{title}.md"):
          f = default_storage.open(f"posts/{title}.md")
          return {"True":f.read().decode("utf-8")}
    else:
            return {"Error": "Post don't any found exists failed"}


def del_post(title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        return {"True": "Post delete successfully"}
    else:
        return {"Error": "Post don't any found exists failed"}

def put_post(title, content):
        filename = f"posts/{title}.md"
        if default_storage.exists(filename):
          file = open(filename, "w")
          file.write(content)  # or we can use append for just adding
          file.close()
          return {"True":"Post update successfully"}
        else:
            return  {"Error":"Post don't any found exists failed"}
