from ninja import Router, Schema
from .import utils

headless_controller=Router()

class data(Schema):
    title:str=None
    content:str=None


@headless_controller.get('')
def display_posts(request):
    return utils.list_posts()


@headless_controller.get('/posts/{title}')
def get_post_by_title(request, title:str):
    return utils.get_post(title)


@headless_controller.post('/posts')
def update_AND_create_post(request, D:data):
    title=D.title
    content=D.content
    return utils.save_post(title, content)



@headless_controller.delete('')
def delete_post(request,title):
    return utils.del_post(title)
