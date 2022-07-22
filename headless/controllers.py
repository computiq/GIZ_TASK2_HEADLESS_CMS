from turtle import update
from ninja import NinjaAPI
from ninja import Router
from django.core.files.storage import default_storage
from headless.utils import *

api = NinjaAPI()
headless_controller = Router()
api.add_router('headless', headless_controller)

@headless_controller.get('/posts')
def get_all_post(request):
    return list_posts()


@headless_controller.get('posts/{title}')
def get_single_post(request,title: str ):
    return get_post(title)
    

@headless_controller.post('/new_posts')
def new_post(request, title: str, content: str):
    return save_post(title, content)


@headless_controller.put("/update/{title}")
def update_post(request, title: str, content: str ):
    return save_post(title, content)


@headless_controller.delete("/delete/posts/{title}")
def delete_post(request, title: str):
    return del_post(title)




