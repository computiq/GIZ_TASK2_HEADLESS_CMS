from ninja import Router
from ninja import Schema
from django.http import JsonResponse
from headless.utils import del_post, get_post, list_posts, save_post

class DataSchema(Schema):
    title : str
    content : str

posts_controller = Router()

# To list all posts
@posts_controller.get('')
def list_post(request):
    return JsonResponse({"All_posts":list_posts()})

# To retrieve a certain post
@posts_controller.get('{title}')
def retrive_post(request, title:str):
    return JsonResponse({f"{title}":get_post(title)})

# To create a new post
@posts_controller.post('')
def create_post(request,data_in : DataSchema):
    title = data_in.title
    content = data_in.content
    save_post(title, content)
    return JsonResponse({"title":f"{title}", "content" : f"{content}"})

# To update a certain post
@posts_controller.post('{title}')
def updata_post(request,title: str , content :str):
    save_post(title, content)
    return JsonResponse({"Saved title":f"{title}", "Saved content" : f"{content}"})

@posts_controller.delete('{title}')
def delete_post(request,title:str):
    get_post_method = get_post(title)
    if get_post_method :
        del_post_method = del_post(title=title)
        return {'message':"Deleted successfully"}
    else:
        return {'message':f"No such file : {title} "}