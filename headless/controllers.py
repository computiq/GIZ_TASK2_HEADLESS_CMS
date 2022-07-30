from ninja import Router
from headless import utils
from headless.utils import *

controller = Router()


@controller.get('/all_posts')
def getAllPost(request):
    return utils.list_posts()


@controller.post('/craete_posts')
def create_post(title, content):
    utils.save_post(title, content)
    return {"success": True}


@controller.put('/update_Posts')
def update_post(title, content):
    utils.save_post(title, content)
    return {"success": True}


@controller.delete('delete_posts')
def delete_post(title):
    utils.del_post(title)
    return {"success": True}
