from ninja import Router, Schema
from headless.utils import *

posts = Router()


class PostSchema(Schema):
    title: str
    content: str

@posts.get('posts')
def posts(request):
    return list_posts()


@posts.get('posts/{title}')
def retrieve_post(request, title: str):
    if get_post(title) == None:
        return 'Not found'
    else:
        return get_post(title)

@posts.post('posts')
def create_post(request, post: PostSchema):
    save_post(post.title, post.content)
    return post.dict()


@posts.put('posts/{title}')
def update_post(request, post: PostSchema):
    save_post(post.title, post.content)
    return post.dict()

@posts.delete('posts/{title}')
def delete_post(request, title: str):
    result = del_post(title)
    if result is None:
        return 'Not found'
    else:
        return result