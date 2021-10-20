from ninja import Router
from.import utils

Post_control=Router()


@Post_control.get('list')
def list_post(request):
    return utils.list_posts()



@Post_control.get('{title}')
def get_post(request ,title):
    return utils.get_post(title)



@Post_control.post('')
def creat_post(request ,title, content):
    return utils.save_post(title, content)

@Post_control.put('{title}')
def update_post(request ,title, content):
    return utils.save_post(title, content)  

@Post_control.delete('{title}')
def Remov_post(request ,title):
    return utils.del_post(title)       

