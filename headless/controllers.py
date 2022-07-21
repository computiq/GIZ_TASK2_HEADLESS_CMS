from ninja import Router
from headless.schemas import postIn
from headless.utils import *
controller = Router()

@controller.get('/list')
def list(request):
    return list_posts()
   
@controller.get('/get_post')
def get_post(request , title:str):
    return get_post(title)

@controller.post('/save_post')
def save(request ,post:postIn):
    save_post(post.title,post.content)
    return "Done!"
    
@controller.delete('/delete')
def delete(request , title: str):
    del_post(title)
    return "Done!"

@controller.put('/update')
def update(request, post :postIn):
    update_post(post.title,post.content)
    return "Done!"
