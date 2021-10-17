from ninja import Router, Schema

from headless.utils import *

posts_controller = Router()


class PostSchema(Schema):
    title: str
    content: str


@posts_controller.get('')
def get_posts(request):
    return {
        "posts": list_posts()
    }


@posts_controller.get('{title}')
def get_posts(request, title: str):
    if get_post(title) is None:
        return {
            "exists": False,
            "post": None
        }
    return {
        "exists": True,
        "post": {
            "title": title,
            "content": get_post(title)
        }

    }


@posts_controller.post('')
def create_post(request, post: PostSchema):
    save_post(post.title, post.content)
    return {
        "created_post": post.dict(),
        "message": "post created successfuly :3"
    }


@posts_controller.put('{title}')
def update_post(request, post: PostSchema, title: str):
    save_post(title, post.content)
    return {
        "updated_post": post.dict(),
        "message": "The post was updated succesfuly :3"
    }


@posts_controller.delete('{title}')
def delete_post(request, title: str):
    if del_post(title):
        return {
            "title": title,
            "deleted": True,
            "message": "The post has been deleted successfully :3"
        }
    else:
        return {
            "title": title,
            "deleted": False,
            "message": "The post doesn't exist .-."
        }
