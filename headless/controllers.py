from ninja import Router ,Schema
from headless.utils import *
from ninja.errors import HttpError

headless_router = Router()
class DataSchema(Schema):
    title: str
    content: str
   


@headless_router.get('posts/')
def li_posts(request):
    return list_posts()

@headless_router.get('posts/{title}')
def li_post(request,title:str):
    retrieve=get_post(title)
    if retrieve == None:
        raise HttpError(404, 'There is no file with this name!')
    else:
        return retrieve

@headless_router.post('posts/')
def save_posts(request,data_in: DataSchema):
    
    save_post(data_in.title,data_in.content)
    return data_in.dict()


@headless_router.put('posts/{title}')
def update_posts(request,data_in: DataSchema):
    save_post(data_in.title,data_in.content)
    return data_in.dict()


@headless_router.delete('posts/{title}')
def del_posts(request,title:str):
    responce = del_post(title)
    if responce is None:
        raise HttpError(404, 'There is no file with this name!')
    else:
        return responce
