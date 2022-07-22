from ninja import Router
from headless.utils import *

cont = Router()


@cont.get("")
def list_all_posts(request):
    return list_posts()


@cont.get("/get_one_post")
def get_one(request, title: str):
    return get_post(title)


@cont.post("/create_post")
def create(request, title: str, content: str):
    return save_post(title, content)


@cont.put("/update_post")
def update(request, title: str, content: str):
    return save_post(title, content)


@cont.delete("/delete_post")
def delete(request, title: str):
    return del_post(title)
