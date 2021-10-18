from enum import unique
from django.core.files import utils
from ninja import Router,Schema
from headless.utils import *
 
class DataSchema (Schema) :
    title: str
    content: str

 
 
controller = Router()
 
@controller.get('')
def posts(request):
    return list_posts()

@controller.get('{title}')
def retrive_post(request,title: str):
    return get_post(title)

@controller.post('')
def create_post(request, data_in: DataSchema):
    return save_post(data_in.title,data_in.content)


@controller.put('{title}')
def update_post(request, data_in: DataSchema):
    name=get_post(data_in.title)
    return save_post(name,data_in.content)

@controller.delete('{title}')
def delete_post(request, tit:str):
    return del_post(tit)