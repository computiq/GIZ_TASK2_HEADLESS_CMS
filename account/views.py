from ninja import Router, Schema
from headless.utils import list_posts, save_post, get_post, del_post

account_controller = Router()

class dataSchema(Schema):
    title: str
    content: str


# to list all posts
@account_controller.get('')
def list_post(request):
    return list_posts()


# to retrieve a certain post
@account_controller.get('{title}')
def retrieve_posts(request, title): 
    return get_post(title)


# to create a new post
@account_controller.post('{title}')
def data_post(request, data_in: dataSchema): 
    save_post(data_in.title, data_in.content)
    return data_in.dict()


# to update a certain post
@account_controller.put('{title}')
def data_update(request, data_in: dataSchema):  
    save_post(data_in.title, data_in.content)
    return data_in.dict()


@account_controller.delete('{title}')
def data_delete(request, title): 
    return del_post(title)