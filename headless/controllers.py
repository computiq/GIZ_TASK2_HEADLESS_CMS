import http
from typing import List
from ninja import Router,Schema
from .utils import list_posts,get_post,save_post,del_post,update_funct
from http import HTTPStatus

blog_controller = Router(tags=['blog'])



@blog_controller.get('/posts')
def list_all_posts(request):
    try:
        list_post = list_posts()
    except:
        return {'message': 'There are no posts to display'}
    return  {'posts': list_post}



@blog_controller.get('/post/{title}')
def get_single_post(request,title:str):
    get_post_method = get_post(title)
    if not get_post_method:
        return {'message':'The file name does not exist'}
    return {'post':get_post_method}



class SchemaCreatePostIn(Schema):
    title : str
    content : str

class SchemaUpdatePostIn(Schema):
    content : str



@blog_controller.post('/create/post')
def create_post(request,pyload:SchemaCreatePostIn):
    title = pyload.title
    content = pyload.content
    get_post_method = save_post(title,content)
    return {'message':'created successfully'}



@blog_controller.put('/update/post/{title}')
def update_post(request,title:str,pyload:SchemaUpdatePostIn):
    new_content = pyload.content
    old_content = get_post(title=title)
    if old_content :
        call_update = update_funct(title,old_content,new_content)
        new_content = get_post(title=title)
        return {'message':'Updated Successfully',"new_content":new_content}

    else :
        return {"message":f"No such file : {title} "}


@blog_controller.delete('/delete/post/{title}')
def delete_post(request,title:str):
    get_post_method = get_post(title)
    if get_post_method : 
        del_post_method = del_post(title=title)
        return {'message':"Deleted successfully"}
    else:
        return {'message':f"No such file : {title} "}
