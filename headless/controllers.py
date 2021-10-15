from ninja import Router
from .utils import list_posts, get_post, del_post, save_post, response
from .schemas import ResponseSchema, PostSchema


headless_controller = Router()



@headless_controller.get("posts" , response={200:ResponseSchema, 404:ResponseSchema})
def fetch_posts(request,per_page:int = 0, page_num:int = 1):
    posts = list_posts()
    msg = "Posts Fetched Successfully"
    if not posts:
        msg = "There is No Posts Yet"
    if per_page:
        return response(True, msg, posts, True, per_page, page_num)
    return 200, response(True, msg,posts)



@headless_controller.get("posts/{slug}" , response={200:ResponseSchema, 404:ResponseSchema})
def retrieve_post(request, slug):
    post = get_post(slug)
    if post:
        return 200, response(True, "Post Retrieved Successfully", [post])
    return 404, response(False, "Post Not Exists")


@headless_controller.post("posts", response={201:ResponseSchema, 400:ResponseSchema})
def create_post(request, post_data: PostSchema):
    post = save_post(**post_data.dict())
    if post:
        return 201, response(True, "Post Created Successfully", [post])
    return 400, response(False, "Post Already Exists")



@headless_controller.put("posts/{slug}", response={200:ResponseSchema, 404:ResponseSchema})
def update_post(request, slug, post_data: PostSchema):
    post =  save_post(update=True, slug=slug ,**post_data.dict())
    if post:
        return 200, response(True, "Post Updated Successfully", [post])
    return 404, response(False, "Post Not Found")



@headless_controller.delete("posts/{slug}" , response={200:ResponseSchema, 404:ResponseSchema})
def delete_post(request, slug):
    post = del_post(slug)
    if post:
       return 200, response(True, "Post Deleted Successfully", [post])
    return 404, response(False, "Post Not Found")
