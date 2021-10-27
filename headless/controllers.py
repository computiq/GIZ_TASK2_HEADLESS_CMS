from ninja import Router, Schema
from .utils import *

headless = Router()

class PostSchema(Schema):
    title: str
    content: str

# to list all posts
@headless.get('posts')
def list_posts(request):
    return {list_posts()}

# to retrieve a certain post
@headless.get('posts/{title}')
def get_post(request, title: str ):
    return ({"{title}" : get_post(title)})

# to create a new post
@headless.post('posts')
def create_post(request, data_in : PostSchema):
    title = data_in.title
    content = data_in.content
    save_post(title, content)
  

# to update a certain post
@headless.put('posts/{title}')
def update_post(request, title : str, content : str):
    save_post(title, content)
    return ( {"title saved" : "{title}", "content saved" : "{content}"} )





