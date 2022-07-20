from ninja import Router

from headless.utils import list_posts
from headless.utils import get_post
from headless.utils import save_post
from headless.utils import del_post


postController = Router()

@postController.get('/posts',tags=["List of Post"],description="View and show all  post ")
def get_all_posts (request):
    return list_posts()

@postController.get('posts/{title}',tags=["Get the Post"],description="View and show all  post ")
def post_by_title(request,title:str):
    return get_post(title)

@postController.post('/posts',tags=["Create Post"],description="Creates a new post just insert title and content ")
def create_post(request,title:str,content:str):
    return save_post(title=title,content=content)


@postController.put('/posts',tags=["Update Post"],description="Updates on content of post by title name")
def update_post(request,title:str,content:str):
    return save_post(title=title,content=content)

@postController.delete('/posts',tags=["Delete Post"],description="Delete post")
def delete_post(request,title:str):
    return del_post(title=title)
