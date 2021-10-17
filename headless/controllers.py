from django.http.response import JsonResponse
from ninja import Router, Schema
from headless.utils import del_post,get_post,save_post,list_posts

headless_controller = Router()

class DataSchema(Schema):
    title : str
    content : str

# to list all posts
@headless_controller.get('posts')
def all_posts(request):
    return ({"list all posts" : list_posts()})

# to retrieve a certain post
@headless_controller.get('posts/{title}')
def retrive_posts(request,title : str):
    return ({"{title}" : get_post(title)})

# to create a new post
@headless_controller.post("posts")
def create_post(request, data_in : DataSchema):
    title = data_in.title
    content = data_in.content
    save_post(title, content)
    return JsonResponse( {"title" : "{title}", "content" : "{content}"} )



# to update a certain post
@headless_controller.put('posts/{title}')
def update_post(request, title : str, content : str):
    save_post(title, content)
    return ( {"title saved" : "{title}", "content saved" : "{content}"} )
