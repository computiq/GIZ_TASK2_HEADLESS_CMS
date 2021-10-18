from typing import Any

from ninja import Router, Schema
from headless.utils import list_posts, get_post, save_post, del_post , put_post

# Create your views here.
post_controller = Router()


class DataSchema(Schema):
    title: str
    content: str


class DataSchemaUP(Schema):
    content: str


@post_controller.get('/post')
def list(request):
    return list_posts()


@post_controller.get('/{title}')
def retrieve_account(request, title: str):
    return get_post(title)


@post_controller.post('/post')
def create_post(request, data_in: DataSchema):
    return save_post(data_in.title, data_in.content)


@post_controller.put('/{title}')
def update_post(request, title: str ,data_in: DataSchemaUP):
    return put_post(title,data_in.content)


@post_controller.delete('/{title}')
def delete_post(request , title: str):
    return del_post(title)
