from ninja import Router, Schema
from headless.utils import  list_posts, save_post, get_post, del_post


posts_controller = Router()

class DataSchema(Schema):
    title: str
    content: str

@posts_controller.get('list_posts')
def list_of_posts(request):
    if list_posts() == []:
        return "There is no posts"
    else:
        return list_posts()

@posts_controller.get('retrieve/{title}')
def retrieve_post(request, title: str):
    if get_post(title) == None:
        return "File Not Found"
    else:
        return get_post(title)
    

@posts_controller.post('create_post')
def create_post(request, data_in: DataSchema):
    save_post(data_in.title, data_in.content)
    return data_in.dict()

@posts_controller.put('update_post')
def update_post(request, data_in: DataSchema):
    save_post(data_in.title, data_in.content)
    return data_in.dict()

@posts_controller.delete('delete_post/{title}')
def delete_post(request, title: str):
    return del_post(title)
    


