from ninja import Router
from headless.utils import*

account=Router()

@account.get('/Get_All')
def getAll(request):
    return(list_posts())

@account.get('/GetOne')
def getOne(request, title: str):
    return(get_post(title))

@account.post('/Creat')
def create(request,title:str, content:str):
    return (save_post(title,content))

@account.put('/Update')
def Update(request, title : str, content:str):
    return(save_post(title, content))

@account.delete('/Delete')
def Delete(request,title:str):
    return(del_post(title))


