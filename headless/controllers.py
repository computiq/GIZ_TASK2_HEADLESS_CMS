from urllib import request
from headless.utils import *
from ninja import Router

Management_Control = Router()

@Management_Control.get("/Listing_Posts")
def listing_posts(request):
    return list_posts()

@Management_Control.get("/Requesting_Post")
def calling_post(request,title: str):
    return get_post(title)

@Management_Control.post("/Creating_Post")
def make_post(request,title: str,content: str):
    return save_post(title,content)

@Management_Control.put("/Updating_Post")
def upating_post(request,title: str,content: str):
    return save_post(title,content,)

@Management_Control.delete("/Deleting_Post")
def remove_post(request,title):
    return del_post(title)
