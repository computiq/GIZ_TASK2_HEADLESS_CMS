from django.shortcuts import render
from ninja import Router
from . import utils
from ninja import Schema    

class Data(Schema):
    title: str
    content: str


headless_controller = Router()

@headless_controller.get('posts')
def get_posts(request):
    return utils.list_posts()



@headless_controller.get('posts/{title}')
def get_one_post(request, title):
    return utils.get_post(title)


@headless_controller.post('posts/')
def save_posts(request, Data_in: Data):
    return utils.save_post(request, Data_in)


@headless_controller.put('posts/{title}')
def update_posts(request, title, content):
    return utils.save_post(title, content)


@headless_controller.delete('posts/{title}')
def delete_posts(request, title):
    return utils.del_post(title)