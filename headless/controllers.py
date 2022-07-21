from urllib import request
from ninja import Router
from . import utils
controler=Router()

@controler.get('/')
def list (request):
          return  utils.list_posts()
@controler.get('/get')
def get (request,title:str):
          return utils.get_post(title)

@controler.post('/create')
def create(request,title:str,cont:str):
          return utils.save_post(title,cont)
@controler.put('/upd')
def upd(request,title:str,cont:str):
          return utils.save_post(title,cont)

@controler.delete('/del')
def dele(request,title:str):
          return utils.del_post(title)