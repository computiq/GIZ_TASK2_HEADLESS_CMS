from . import utils
from ninja import Router


headless_controller = Router()


@headless_controller.get('/')
def list1():
    return utils.list_posts()


@headless_controller.get('/')
def get():
    return utils.get_post('post')


@headless_controller.post('/')
def save():
    return utils.save_post('new_post', '')


@headless_controller.put('/')
def update():
    return utils.get_post('post')
