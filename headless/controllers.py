from ninja import Router
from headless import utils

user_controller=Router()

@user_controller.get('/')
def Get_Allpost(request):
    return utils.list_posts()
    

@user_controller.get('/{title}')
def Get_Onepost(request,title:str):
    return utils.get_post(title)

@user_controller.post('/')
def Addpost(request,title:str,content:str):
    return utils.save_post(title,content)

@user_controller.put('/{title}')
def Editpost(request,title:str,content:str):
    return utils.save_post(title,content)

@user_controller.delete('/{title}')
def Deletepost(request,title:str):
    return utils.del_post(title)