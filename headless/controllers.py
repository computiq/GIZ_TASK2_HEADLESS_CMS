from ninja import Router
from . import utils
import django
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from ninja import NinjaAPI
api=NinjaAPI()
Controller=Router()

@Controller.get('/getAll')
def GetAll(request):
    return utils.list_posts()


@Controller.get('/getOne')
def Getone(request, filename: str):
    return NoneChecker(utils.get_post(filename))



@Controller.post('/Post')
def CreatePost(request, filename: str, contant: str):
    utils.save_post(filename,contant)
    return HttpResponse("file created",status=201)


@Controller.put('/Update')
def UpdatePost(request,filename:str, contant:str):
    return NoneChecker(utils.update_post(filename,contant))


@Controller.delete('/Delete')
def DeletePost(request,filename:str):
    return NoneChecker(utils.del_post(filename))

def NoneChecker(file):
    if file==None:
        return HttpResponse("file not found", status=404)
    else:
        return file