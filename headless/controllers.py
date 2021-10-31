from ninja import Router
from headless.utils import del_post, list_posts, get_post, save_post, del_post

account_controller = Router()

@account_controller.get('')
def ListPosts(request):
    return list_posts()

@account_controller.get('{title}')
def GetPost(request, title: str):
    return get_post(title)

@account_controller.put('{title}')
def UpdatePosts (request, title: str, content: str):
    return save_post(title, content)

@account_controller.delete('{title}')
def DeletePost (request, title: str):
    return del_post(title)

#I'll take the W on this one :D