from typing import Text
from ninja import Router,Schema
import headless.utils as utils_functions
from ninja.errors import HttpError


posts_controller=Router()
class the_post(Schema):
    title:str
    the_content:Text


@posts_controller.get('posts')
def get_posts(request):
    return utils_functions.list_posts()

@posts_controller.get('posts/{title}')
def get_post(request,title:str):
   the_post= utils_functions.get_post(title)
   if the_post ==None:
    raise HttpError(503,  "there is no post in this title , try anothr title")
   else:
      return the_post


@posts_controller.post('posts')
def add_a_post(request,post_content:the_post):
  the_title=post_content.title
  the_content=post_content.the_content
  utils_functions.save_post(the_title,the_content)
  return post_content

@posts_controller.put('posts/{title}')
def update_post(request,post_content:the_post,title:str):
  the_content=post_content.the_content
  utils_functions.save_post(title,the_content)
  return post_content


@posts_controller.delete('delete_post/{title}')
def delete_post(request,title:str):
  if utils_functions.del_post(title):
    return "the post deleted succesfuly"
  else :
    return"there is no post in this title"
