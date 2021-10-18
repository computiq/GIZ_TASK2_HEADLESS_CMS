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
from django.shortcuts import render
from ninja.router import Router
from headless.schemas.post_schemas import PostSchema

account_controller = Router()

"""
data = [
    {'name': 'Layth', 'age': 39},
    {'name': 'Suhaib', 'age': 90},
]
"""

@account_controller.get('listt')
def list_account(request):
    list = []
    for n in range(len(utils.list_posts())):
        list.append({"name": utils.list_posts()[n]})
    return list




@account_controller.get('posts/{name}') 
def retrieve_account(request, name: str):
    return {"content": utils.get_post(name)} 


@account_controller.post('posts') 
def create_account(request, data_in: PostSchema ):
    name = data_in.name
    content = data_in.content
    utils.save_post(name,content)
    return data_in.dict()
    
 @account_controller.put('posts/{name}')
def update_account(request, name: str, data_in: PostSchema):
    name = data_in.name
    content = data_in.content
    utils.save_post(name,content)
    return data_in.dict()


@account_controller.delete('account/{name}')
def delete_account(request, name: str):
    return utils.del_account(name)
    from ninja import Schema

class PostSchema(Schema):
    name: str
    content: str
    age:int
