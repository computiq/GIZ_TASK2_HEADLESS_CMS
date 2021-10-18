import re
from ninja import Router , Field , Schema 
from ninja.errors import HttpError
from headless.utils import del_post, get_post, list_posts, save_post


class fileIN(Schema):
    #this is to check min length and maxk length for the title input 
    title: str = Field (min_length=1 , max_length=250)
    content: str



headless = Router()

@headless.get("posts")
def headless_getall(request):
    return list_posts()


@headless.get("posts/{title}")
def headless_get(request , title: str):
    the_post = get_post(title)
    if the_post:
        return {"content": the_post}
    raise HttpError(404, "File not found")


@headless.post("posts")
def headless_post(request , payload: fileIN):
    checker = re.search('[\/:*?<>|]' , payload.title)
    if checker:
        raise HttpError(400, "there are special characters that can't be assigned as file name")
    the_post = get_post(payload.title)
    if the_post:
        raise HttpError(409 , "file is already created")
    save_post(**payload.dict()) 
    return {"title": payload.title , "content": payload.content}


@headless.put("/update/{title}")
def headless_update(request , title: str , payload: fileIN):
    the_post = get_post(title)
    update_post = get_post(payload.title)
    if the_post:
        if not update_post or update_post == the_post:
            save_post(**payload.dict())
            return {"title": payload.title , "content": payload.content}
        raise HttpError(409, "you can't rename the file to one that is already existed")
    raise HttpError(404, "file not found")


@headless.delete("posts/{title}")
def headless_delete(request, title: str):
    the_post = del_post(title)
    if the_post:
        raise HttpError(404, "File not found")
    return {"detail": f" the file '{title}' has been deleted successfully"}
