from typing import ContextManager
from django.shortcuts import render
from ninja.router import Router
from headless.schemas.post_schemas import PostSchema
import headless.utils as utils
import json

post_controller = Router()

"""
data = [
    {'name': 'Layth', 'age': 39},
    {'name': 'Suhaib', 'age': 90},
]

"""

@post_controller.get('') #pathParameter
def list_posts(request):
    list = []
    for i in range(len(utils.list_posts())):
        list.append({"name": utils.list_posts()[i]})
    return list

    


@post_controller.get('posts/{name}') 
def retrieve_post(request, name: str):
    return {"content": utils.get_post(name)} 

    
@post_controller.post('posts') 
def create_post(request, data_in: PostSchema ):
    name = data_in.name
    content = data_in.content
    utils.save_post(name,content)
    return data_in.dict()

@post_controller.put('posts/{name}')
def update_post(request, name: str, data_in: PostSchema):
    name = data_in.name
    content = data_in.content
    utils.save_post(name,content)
    return data_in.dict()


@post_controller.delete('posts/{name}')
def delete_post(request, name: str):
    return utils.del_post(name)