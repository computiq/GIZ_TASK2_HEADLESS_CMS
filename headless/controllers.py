from ninja import Router
from headless import utils

CMS_controllers = Router()

# to list all posts
@CMS_controllers.get('/list')
def list(request):
    return utils.list_posts()

# to retrieve a certain post
@CMS_controllers.get('/retrieve/{title}')
def retrieve(request,title:str):
    return utils.get_post(title)

# to create a new post
@CMS_controllers.post('/create')
def create(request,title:str, content:str):
    return utils.save_post(title,content)

# to update a certain post
@CMS_controllers.put('/update/{title}')
def update(request,title:str, content:str):
    return utils.save_post(title,content)

# to delete a certain post
@CMS_controllers.delete('/delete/{title}')
def delete(request,title:str):
    return utils.delete_post(title)

