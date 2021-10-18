from ninja.router import Router
from ninja import Router, Schema
from .utils import *

headless_controller = Router()


class DataSchema(Schema):
    title: str
    content: str


@headless_controller.get('')
def listPosts(request):
    return list_posts()


@headless_controller.get('{title}')
def getPost(request, title: str):
    return get_post(title)


@headless_controller.post('')
def createPost(request, data_in: DataSchema):
    save_post(data_in.title, data_in.content)
    return 'success'


@headless_controller.put('')
def updatePost(request, data_in: DataSchema):
    save_post(data_in.title, data_in.content)
    return 'success'


@headless_controller.delete('{title}')
def deletePost(request, title):
    del_post(title)
    return 'success'
