
from headless.utils import *
from ninja import Router 

RtApp = Router()

# to list all posts
@RtApp.get("/get_all")
def get_all(request):
     return list_posts()

# to retrieve a certain post
@RtApp.get("/get_one")
def get(request,title: str):
    return get_post(title)


# to create a new post
@RtApp.post("/post")
def creat_Post(request,title: str,content: str):
    return save_post(title,content,)


# to update a certain post
@RtApp.put("/update")
def apdate(request,title: str,content: str):
    return save_post(title,content)

# to delete a certain post
@RtApp.delete("/delet")
def remove(request,title):
    return del_post(title)

