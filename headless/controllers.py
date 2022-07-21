from calendar import c
from ctypes import util
from ninja import Router
from headless.utils import * 


head_countrollers = Router()

@head_countrollers.get("/call_all")
def list(request):
    return list_posts()

@head_countrollers.get("/search_by_title")
def search(request,title):
    return get_post(title)


@head_countrollers.post("/add_post")
def save(request, title,content):
    return save_post(title,content)

@head_countrollers.put("/update_post")
def update(request, title,content):
    return save_post(title,content)

@head_countrollers.delete("delet_post")
def delete(request,title):
    return del_post(title)
