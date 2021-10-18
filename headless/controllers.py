from ninja import Router
from ninja import Schema
import headless.utils as helper

controller_headless=Router()

class dataSchema(Schema):
    title:str
    content:str

@controller_headless.get("GET /posts")
def gitAllPosts(request):
    return helper.list_posts()


@controller_headless.get("GET /posts/{title}")
def gitPostById(request,title):
    return {title:helper.get_post(title)}



@controller_headless.post("POST/posts")
def createNewPost(request, data:dataSchema):
    helper.save_post(data.title,data.content)
    return data.dict()

@controller_headless.put("/update_posts")
def updatePost(request,data:dataSchema,title):
    if title in helper.list_posts():
        helper.del_post(title)
        return helper.save_post(data.title,data.content)

@controller_headless.delete("DELETE /posts/{title}")
def deletePost(request,title):
    return helper.del_post(title)