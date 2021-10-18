
from ninja import Router, Schema
from headless import utils

post_controller = Router()

class PostSchema(Schema):
    title: str
    content: str

@post_controller.get('posts')
def posts(request):
    return list_posts()


@post_controller.get('posts/{title}')
def retrieve_post(request, title: str):
        return get_post(title)


@post_controller.post('posts')
def create_post(request, title: str, content: str):
    save_post(post.title, post.content)
    return post.dict()


@post_controller.put('posts/{title}')
def update_post(request,  title: str, content: str):
    save_post(post.title, post.content)
    return post.dict()
    


@post_controller.delete('posts/{title}')
def delete_post(request, title: str):
  return utils.del_post(title)