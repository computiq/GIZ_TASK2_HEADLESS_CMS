from django.shortcuts import render
from ninja import Router
from . import utils


headless_controller = Router()

@headless_controller.get('posts')
def get_posts(request):
    return utils.list_posts()



@headless_controller.get('posts/{title}')
def get_one_post(request, title):
    return utils.get_post(title)


@headless_controller.post('posts/{title}/{content}')
def save_posts(request, title, content):
    return utils.save_post(title, content)


@headless_controller.put('posts/{title}')
def update_posts(request, title, content):
    return utils.save_post(title, content)


@headless_controller.delete('posts/{title}')
def delete_posts(request, title):
    return utils.del_post(title)