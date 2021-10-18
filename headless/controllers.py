from typing import ContextManager
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from ninja.router import Router
from headless.schemas.post_schemas import PostSchema
import headless.utils as utils
from ninja.errors import HttpError

post_controller = Router()


@post_controller.get('')
def list_posts(request):
    list = []
    for i in range(len(utils.list_posts())):
        list.append({"name": utils.list_posts()[i]})
    return JsonResponse(list, safe=False)

    


@post_controller.get('{name}') 
def retrieve_post(request, name: str):
    record = {"content": utils.get_post(name)} 
    return JsonResponse(record, safe=False)

    
@post_controller.post('') 
def create_post(request, data_in: PostSchema ):
    name = data_in.name
    content = data_in.content
    utils.save_post(name,content)
    return JsonResponse(data_in.dict())

@post_controller.put('{name}')
def update_post(request, name: str, data_in: PostSchema):
    name = data_in.name
    content = data_in.content
    utils.save_post(name,content)
    return JsonResponse(data_in.dict())


@post_controller.delete('{name}')
def delete_post(request, name: str):
    utils.del_post(name)
    return("Delete Succesfully")
     