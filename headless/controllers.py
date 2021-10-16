from ninja import Router, Schema
from ninja.main import NinjaAPI
from django.http import JsonResponse
from headless.utils import save_post , get_post, list_posts,del_post,change_post



class Post(Schema):
    title:str
    content:str
class PostS(Schema):
    content:str


cms_controller = Router()


# list All Posts
@cms_controller.get("posts")
def show_posts(request):
    return list_posts()

# retrieve a certain post
@cms_controller.get("posts/{title}")
def show_post(request ,title):
   return get_post(title)

# update a certain post
@cms_controller.put("posts/{title}")
def update_post(request ,title,post:PostS):
    if change_post(title) == False:
        return " file not found"
    else:
        content=post.content
        save_post(title,content)
        return "updated !"


# create new post with title and content 
@cms_controller.post("posts")
def create_post(request , post:Post):
     return save_post(post.title,post.content)


# delete post
@cms_controller.delete("posts/{title}")
def delete_post(request,title):
    return del_post(title)
    



 
   



