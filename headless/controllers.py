from ninja import Router, Schema
from headless.utils import *

posts_controller = Router()


class postSchema(Schema):
    title: str
    content: str


@posts_controller.get('')
def get_all_posts(request):
    return list_posts()


@posts_controller.get('{title}')
def get_specific_post(request, title: str):
    return get_post(title)


@posts_controller.post('')
def create_post(request, request_body: postSchema):
    save_post(request_body.title, request_body.content)
    return request_body.dict()


@posts_controller.put('{title}')
# {title}  path parameter acts as ID to select a post
def update_specific_post(request, title: str, request_body: postSchema):
    # maybe returning all posts after update would be better than returning null
    return update_post(title, request_body.title, request_body.content)


@posts_controller.delete('{title}')
def delete_post(request, title: str):
    return del_post(title)
