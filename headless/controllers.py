from . import utils

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from ninja import Router,Schema
headless_controller=Router()

@headless_controller.get('posts')
def get_posts(request):
    return utils.list_posts()


@headless_controller.get('posts/{title}')
def get_one_post(request, title: str):
    return utils.get_post(title)


@headless_controller.post('')
def create_aaccount(request, data_in: DataSchema):
    utils.save_post(data_in.title, data_in.content)
    return data_in.dict()


@headless_controller.put('{title}')
def update_specific_post(request, title: str, data_in: DataSchema):
    return utils.update_post(title, data_in.title, data_in.content)


@headless_controller.delete('{title}')
def delete_posts(request, title: str):
    return utils.del_post(title)