from ninja import Router, Schema
from .utils import *

less = Router()

class PostSchema(Schema):
    title_name: str
    content: str

@less.get('posts')
def list_posts(request):
    return {list_posts()}

# to retrieve a certain post
@less.get('posts/{title_name}')
def get_post(request, title_name: str ):
    return ({"{title_name}" : get_post(title_name)})

# to create a new post
@less.post('posts')
def create_post(request, data_in : PostSchema):
    title_name = data_in.title_name
    content = data_in.content
    save_post(title_name, content)


# to update a certain post
@less.put('posts/{title_name}')
def update_post(request, title_name : str, content : str):
    save_post(title_name, content)
    return ( {"title saved" : "{title_name}", "content saved" : "{content}"} )
