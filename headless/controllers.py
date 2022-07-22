from email import utils
from urllib import request
from ninja import NinjaAPI
from headless.utils import *
from ninja import Router

CMSAPP = Router()

@CMSAPP.get("/returns_allpost")
def list_posts(request):
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

@CMSAPP.get("/retriev_post/{title}")
def get_post(request,title):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None
    """
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
        

@CMSAPP.post("/create_post/{title}/{content}")
def save_post(request,title, content):
    """
    create a new post, given its title and Markdown
    content. If an existing post with the same title already exists,
    It is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename,ContentFile(content))

@CMSAPP.put("/update_post/{title}/{content}")
def save_post(request,title, content):
    """
    Update a post, given its Title and Markdown
    Content.An existing post with the same title already exists,
    It will be updated.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename,ContentFile(content))
    
@CMSAPP.delete("/delete_post/{title}")
def del_post(request,title):
    """
    Delete a certain post, given its title 
    If an existing post with the same title already exists,
    It will be deleted.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        