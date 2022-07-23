from email import utils
from turtle import title
from urllib import request
from ninja import Router
from headless.utils import *

headlss_controller = Router()

@headlss_controller.get('/')
def list(request):
    return list_posts()

@headlss_controller.get('GET/posts/title')
def getPost(request, title: str):
    return get_post(title)

@headlss_controller.put('update/post')    
def save(request, title: str , content: str):
    return save_post(title,content)

@headlss_controller.post('/')
def post(request, title: str , content: str):
    return save_post(title,content)

@headlss_controller.delete('/')
def delete(request , title: str):
    return del_post(title)