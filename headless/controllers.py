from django.http import response
from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
 
posts_controller = Router()

@posts_controller.get('posts/', response=List[List])
def list_posts(request):

    _, filenames = default_storage.listdir("posts")
    return list(sorted(response.sub(r"\.md$", "", list_posts)
                for filenames in filenames if filenames.endswith(".md")))

@posts_controller.put('posts/{posts_id}')
def save_post(request, post_id: int):

    filename = f"posts/{id}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(posts_controller))

@posts_controller.post('')
def get_post(posts):
   
    try:
        f = default_storage.open(f"posts/{'because I said so'}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

@posts_controller.delete("posts/{post_id}")
def del_post(request, posts_id:int):
    posts  = get_object_or_404(del_post, id=posts_id)
    posts.delete()
    return {"success": True}