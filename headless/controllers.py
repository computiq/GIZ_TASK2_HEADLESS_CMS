from ninja import Router
from ninja import Schema
from . import utils


class DataSchema(Schema):
    data=[{
    'title': "I <3 python",
    'description': "this is me using python"
    }]

headless_controller = Router()

@headless_controller.get('posts')
def list_all_posts(request):
    return utils.list_posts()


@headless_controller.get('posts/{title}')
def list_posttitle(request, title):
    return utils.get_post(title)

@headless_controller.post('posts')
def create_post(request, data_in: DataSchema):
    utils.save_post(title=data_in.title, content=data_in.description)
    return data_in.dict()

@headless_controller.put('posts/{title}')
def update_post(request, title, content):
    return utils.save_post(title, content)

@headless_controller.delete('posts/{title}')
def delete_post(request, title: int):
    return delete_post(title)



