from headless import utils 
from ninja import Router, Schema

# Creating a class for storing the body on a post call
class posts(Schema):
    title: str
    content: str

headless_controller = Router()


# First route
@headless_controller.get("posts")
def list_posts(request):
    # Just returning what the function gives us
    return utils.list_posts()


# Second route
@headless_controller.get("post/{title}")
def list_by_title(request, title: str):
    # Same as up
    return utils.get_post(title)


#Third route
@headless_controller.post("posts")
def update(request, Data_in: posts):
    # Just using an inhearted class
    utils.save_post(Data_in.title, Data_in.content)


#Fourth route
@headless_controller.put("posts/{title}")
def update(request, title: str, content: str):
    # Using both query and path variables
    utils.save_post(title, content)


# Fifth route
@headless_controller.delete("posts/{title}")
def delete(request, title: str):
    # Just calling the function
    utils.del_post(title)