from ninja import Router
from .utils import list_posts
from .utils import get_post
from .utils import save_post
rt =Router()
@rt.get('/post')
def pos(request):
    return (list_posts())
@rt.get('/po/{title}')
def wr(request,title):
    return (get_post(title))
@rt.post('/w')
def my(request,title,content):
    save_post()
@rt.put('/wm/{title}')
def ms(request,title,content):
    save_post(title,content)





