from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from account.controllers import account_controller

api = NinjaAPI()
api.add_router('post', account_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

from ninja import Schema

class PostSchema(Schema):
    name: str
    age:int
    content: str



from django.shortcuts import render
from ninja import Router
from . import utils

account_controller = Router()

data = [
    {'name': 'Layth', 'age': 39},
    {'name': 'Suhaib', 'age': 90},
]

@account_controller.get('listt') 
def list_posts(request):
    return utils.list_posts()



@account_controller.get('posts/{name}') 
def retrieve_post(request, name: str):
    return { utils.get_post(name)} 


@account_controller.post('posts') 
def create_post(request, data_in: PostSchema ):
    utils.save_post(title)
    return data_in.dict()

@account_controller.put('posts/{title}')
def update_post(request, title: str, data_in: PostSchema):
    utils.save_post(title)
    return data_in.dict()


@account_controller.delete('posts/{title}')
def delete_post(request, title: str):
    return utils.del_post(title) 
