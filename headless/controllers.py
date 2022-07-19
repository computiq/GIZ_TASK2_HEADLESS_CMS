from ninja import NinjaAPI
from headless.utils import *

posts = NinjaAPI()


# Get all posts
@posts.get('/list all posts')
def all_posts(request):
    return list_posts()


@posts.get('/retrieve a certain post')
def retrieve_post(request, title: str):
    return get_post(title)


@posts.post('/create a new post')
def create_post(request, title: str, content: str):
    return save_post(title, content, ' file is created')


@posts.put('/update a certain post')
def update_post(request, title: str, content: str):
    return save_post(title, content, ' file is updated')


@posts.delete('/delete post')
def delete_post(request, title: str):
    return del_post(title, ' file is deleted')
