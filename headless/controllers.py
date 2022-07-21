from urllib import request
from ninja import Router
from . import utils

posts_controller=Router()

@posts_controller.get('/')
def list (request):
          return  utils.list_posts()
@posts_controller.get('/get')
def get (request,title:str):
          return utils.get_post(title)

@posts_controller.post('/create')
def create(request,title:str,cont:str):
          return utils.save_post(title,cont)
@posts_controller.put('/upd')
def upd(request,title:str,cont:str):
          return utils.save_post(title,cont)

@posts_controller.delete('/del')
def dele(request,title:str):
          return utils.del_post(title)