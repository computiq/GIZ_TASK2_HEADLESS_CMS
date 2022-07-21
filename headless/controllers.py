from ninja import Router
from headless import utils
from django.http import HttpResponse

Controller=Router()

@Controller.get('/getAllPost')
def getAllPost(request):
    return utils.list_posts()


@Controller.get('/getOnePost')
def GetOnePost(request, filename: str):
    return NoThing(utils.get_post(filename))

@Controller.post('/Post_Create')
def CreatePost(request, filename: str, contant: str):
    utils.save_post(filename,contant)
    return HttpResponse("file created",status=201)


@Controller.put('/Update_Post')
def UpdatePost(request,filename:str, contant:str):
    utils.update_post(filename, contant)
    return HttpResponse("file update", status=201)


@Controller.delete('/Delete_Post')
def DeletePost(request,filename:str):
    return NoThing(utils.del_post(filename))

def NoThing(File):
    if File==None:
        return HttpResponse("This file not found", status=404)
    else:
        return File
