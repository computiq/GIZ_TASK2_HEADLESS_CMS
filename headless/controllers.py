from ninja import Router
from .utils import *
from ninja.errors import HttpError

router = Router()

@router.post('/posts')
def create_post(request,title,content): save_post(title,content)
    
@router.get("/posts")
def list_All_posts(request): return list_posts()

@router.get("posts/{title}")
def get1Post(request,title): return get_post(title)

@router.put("posts/{title}")
def update1post(request,title,content):save_post(title,content)


@router.delete("posts/{title}")
def delete1post(request,title):
    try:
        del_post(title)
        return "post was deleted successfuly"
    except:
        raise HttpError(404, "Post Was Not Found.")