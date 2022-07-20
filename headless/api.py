from ninja import NinjaAPI
from headless.utils import list_posts, save_post, get_post, del_post, update_post
from ninja import Router
api = NinjaAPI()
cont = Router()

@cont.post("/posts/{title}")
def save(request, title, contents):      
    save_post(title , contents)
    
@api.get("/posts")
def get(request, title):    
    return get_post(title)

@cont.get("/posts")
def list(request):        
    return list_posts()
    

@cont.put("/posts/{title}")
def update(request, title, contents):      
    return update_post(title , contents)

@cont.delete("/posts/{title}")
def delete(request, title):    
    del_post(title)



