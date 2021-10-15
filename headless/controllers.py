from django.http import request
from ninja import Router,Schema
from headless.utils import del_post, get_post, list_posts, save_post

headless_conttroller=Router()

class DataSchema(Schema):
    title:str

class DataSchema1(Schema):
    title:str
    content:str

class DataSchema2(Schema):
    title:str

@headless_conttroller.get('list')
def show_posts(request):
    return list_posts()

@headless_conttroller.get('')
def show_post(request,title:str):
    return get_post(title)

@headless_conttroller.post('')
def create_post(request, data_in:DataSchema1):
    
    return save_post(data_in.title,data_in.content)

@headless_conttroller.delete('')
def remove_post(request,data_in:DataSchema2):
    return del_post(data_in.title)