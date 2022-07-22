from ninja import Router
from headless import utils
headless_control = Router()


@headless_control.get('/posts')
def get_all_list(request):
    return utils.list_posts()


@headless_control.get('/post/{title}')
def post(request, title):
    return utils.get_post(title)


@headless_control.post("new")
def new(request, title: str, content: str):
    utils.save_post(title, content)


@headless_control.put("/update/{title}")
def update(request, title: str, content: str):
    utils.save_post(title, content)


@headless_control.delete("/delete/{title}")
def delete(request, title: str):
    utils.del_post(title)

