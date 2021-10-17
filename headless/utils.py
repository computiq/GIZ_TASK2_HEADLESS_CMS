import re
from django.core.files.base import ContentFile
import os
from django.core.files.storage import default_storage

def list_posts():
    #Returns a list of all names of blog posts.
    _, filenames = default_storage.listdir("posts")
    postsList = []
    for filename in filenames:
        if filename.endswith(".md"):
            file = open(os.getcwd()+"/posts/"+filename, "r")
            content = file.read()
            a = {'title': filename, 'content': content}
            postsList.append(a)

    return postsList


# def save_post(title, content):
def save_post(request, Data_in):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{Data_in.dict()['title']}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        default_storage.save(filename, ContentFile(Data_in.dict()['content']))
        return "updated"
    else:
        default_storage.save(filename, ContentFile(Data_in.dict()['content']))
        return "saved"


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
        return "deleted"
