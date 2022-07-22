from ninja import  Router
from typing import List
# from headless.schemas import PostIn
from headless import utils
from headless.models import Posts
from headless.schemas import PostsIn, NotFound, PostsOut

posts_controller =Router()

# get one post
@posts_controller.get('/post/{title}')
def get_post(request, title : str ):
    return  utils.get_post(title)

#get all posts
@posts_controller.get('/posts')
def list_posts(request ):
    return list(utils.list_posts())

#create post
@posts_controller.post('/post')
def create_post(request, payload: PostsIn ):
    return utils.save_post( title=payload.title, content= payload.content)


#update post
@posts_controller.put('/post/{title}')
def update_post(request,  title : str ,payload: PostsIn ):
    return utils.save_post(title= title,content= payload.content)

#delete post
@posts_controller.delete('soft/{title}')
def delete_post(request , title:str):
    return utils.del_post(title=title)

