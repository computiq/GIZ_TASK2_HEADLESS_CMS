from ninja import Router
from headless import utils

cms_controller = Router()

@cms_controller.get('posts')
def list_posts(request):
  return utils.list_posts()

@cms_controller.get('posts/{title}')
def get_post(request, title: str):
  return utils.get_post(title)

@cms_controller.post('posts')
def save_post(request, title: str, content: str):
  return utils.save_post(title, content, request.method)

@cms_controller.put('posts/{title}')
def update_post(request, title: str, content: str):
  return utils.save_post(title, content, request.method)

@cms_controller.delete('posts/{title}')
def delete_post(request, title: str):
  return utils.del_post(title)
