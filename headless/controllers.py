
from ninja import NinjaAPI
from ninja import Router 
from . import utils
api = NinjaAPI()
controll_router = Router() 

@controll_router.get('/posts')
def List_Post(request):
    return utils.list_posts()

@controll_router.get('/posts/{title}')
def get_content_of_certain_post(request,title:str):
    return utils.get_post(title)

@controll_router.post('/posts')
def new_post(request,title:str,contant:str):
    return utils.save_post(title,contant)

@controll_router.put('/posts/{title}')
def update_post(request,title:str,contant:str):
    return utils.save_post(title,contant)

@controll_router.delete('/posts/{title}')
def delete_post(request,title:str):
    return utils.del_post(title)
