from ninja import Router
from . import utils


post_controller = Router()


@post_controller.get("/posts")
def get_posts(request):
    return {'posts': utils.list_posts()}


@post_controller.get("/posts/{title}")
def get_post(request, title):
    return {'post': utils.get_post(title)}


@post_controller.post("/posts")
def create_post(request, title, content):
    utils.save_post(title, content)
    return {"success": True}


@post_controller.put("/post/{title}")
def update_post(request, title, content):
    utils.save_post(title, content)
    return {"success": True}


# DELETE
@post_controller.delete("/posts/{title}")
def delete_post(request, title):
    utils.del_post(title)
    return {"success": True}
