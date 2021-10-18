from django.shortcuts import render
from ninja import Router
from ninja import Schema 
from headless import utils
# Create your views here.
class DataSchema(Schema):
    title:str
    continite:str
headless_controller=Router()


data=utils.list_posts()
@headless_controller.get('')
def list_headless(request):
    return data
@headless_controller.get('retrive/{title}')
def list_headless(request,title:str):
    utils.get_post(title)
          
@headless_controller.post('')
def create_headless(request,title:str,contente:str):
    utils.save_post(title,contente)

    