from ninja import Schema
from ninja import Router
from . import utils

headless_control = Router()


class DataSchema(Schema):
    title: str
    content: str


@headless_control.get('posts')
def get_posts(request):
    return utils.list_posts()


@headless_control.get('posts/{title}')
def get_post_by_title(request, title: str):
    return utils.get_post()


@headless_control.post('')
def save_posts(request, data_in: DataSchema):
    return utils.save_post(data_in.title, data_in.content)


@headless_control.put('{title}')
def update_posts(request, title: str, data_in: DataSchema):
    return utils.update_post(title, data_in.title, data_in.content)
