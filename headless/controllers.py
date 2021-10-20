from ninja import Router, Schema
from ninja.errors import HttpError
from headless.utils import *

post_controller = Router()

class PostSchema(Schema):
    title: str
    content: str

@post_controller.get('posts')
def posts(request):
    return list_posts()

@post_controller.get('posts/{title}')
def retrieve_post(request, title: str):
    if get_post(title) == None:
        raise HttpError(404, 'Not found')
    else:
        return get_post(title)

@post_controller.post('posts')
def create_post(request, post: PostSchema):
    save_post(post.title, post.content)
    return post.dict()

@post_controller.put('posts/{title}')
def update_post(request, post: PostSchema):
    save_post(post.title, post.content)
    return post.dict()

@post_controller.delete('posts/{title}')
def delete_post(request, title: str):
    result = del_post(title)
    if result is None:
        raise HttpError(404, 'Not found')
    else:
        return result