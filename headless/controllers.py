from django.http.response import StreamingHttpResponse
from ninja import Router
from ninja import Schema
from headless.utils import list_posts, save_post, get_post,del_post

head_controller= Router()

class post_se(Schema):
    title :str
    contents : str

# get all post
@head_controller.get('')
def head_all_list(request):
     #data = save_post('create_new_post', 'hi this is my first post try')
     return list_posts()

#get single post based on title
@head_controller.get('{title}')
def head_post(request, title):
    return get_post(title)

#insert new  post
@head_controller.post('title')
def head_insert_post(request, body: post_se):
    save_post(body.title, body.contents)
    return body.dict()

# update specifi post
@head_controller.post('title')
def head_delete_post(request, body: post_se):
    save_post(body.title, body.contents)
    return body.dict()

     

     
