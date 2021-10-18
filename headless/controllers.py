from enum import unique
from django.core.files import utils
from ninja import Router,Schema
from headless.utils import *
 
class DataSchema (Schema) :
    title: str
    content: str

 
 
controller = Router()
 
@controller.get('post')
def posts(request):
    return list_posts()

@controller.get('post/{title}')
def retrive(request,title: str):
    return get_post(title)

@controller.post('createpost')
def createPost(request, data_in: DataSchema):
    return save_post(DataSchema.title,DataSchema.content)