from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from urllib import request
from ninja import Router
import re


router = Router()


@router.get('/')
def list_posts(request):
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


@router.get('/get')
def get_post(request, title: str):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


@router.post('/create')
def save_post(request, title: str, content: str):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    return f"The post with the title '{title}' has been created"


@router.put('update')
def update_post(request, title : str, content : str):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.save(filename, ContentFile(content))
    else: 
        return f"The post with the title '{title}' does not exist"
    return f"The post with the title '{title}' has been updated"

@router.delete('/delete')
def del_post(request, title: str):
    post = f"posts/{title}.md"
    if default_storage.exists(post): default_storage.delete(post)
    else: 
        return f"The post with the title '{title}' does not exist"
    return f"The post with the title '{title}' has been deleted"