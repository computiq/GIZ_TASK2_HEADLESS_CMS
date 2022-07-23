from ninja import Router
from headless.utils import *

controller = Router()

@controller.get('posts')
def get_posts(request):
    return list_posts()

@controller.get('post')
def get_single_post(request, title):
    return get_post(title)

@controller.post('create')
def create_post(request, title, content):
    return save_post(title, content)
    
@controller.put('update')
def update_post(request, title, content):
    return save_post(title, content)

@controller.delete('deleted')
def delet_post(request, title):
    return del_post(title)