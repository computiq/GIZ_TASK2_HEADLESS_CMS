from ninja import Router,Schema
from headless.utils import *

headless_controller = Router()

class DataSchema(Schema):
    title:str
    content:str

@headless_controller.get('posts')
def getPosts(request):
    return list_posts()

@headless_controller.get('posts/{title}')
def get_post (request , data:DataSchema):
    return get_post(data.title)

@headless_controller.post('posts/{title}/{content}')
def save_(request, data:DataSchema):
    return save_post(data.title, data.content)


@headless_controller.put('posts/{title}')
def save_posts(request, data:DataSchema):
    return save_post(data.title, data.content)


@headless_controller.delete('posts/{title}')
def delete_posts(request, data:DataSchema):
    return del_post(data.title)
