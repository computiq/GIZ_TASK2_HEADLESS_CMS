from ninja import Router,Schema
from headless.utils import get_post,list_posts,save_post,del_post

headless_controller = Router()

class data_schema(Schema):
     title : str
     content : str
"""
   end point for get all post titles  by using function list_post()
"""




@headless_controller.get('list')
def list_account (request):
    return list_posts()
"""
   end point for get spical  post  by title   using function get_post()
"""

@headless_controller.get('retrive/{title}')
def retrive_headless (request , title : str):
    return get_post(title)
"""
   end point for create new  post by sending title and content   using function save_post() and i returrn all post to show the new addded file 
"""
@headless_controller.post('')
def create_new_post(request ,datain : data_schema):
     save_post(datain.title,datain.content)
     return list_posts()
"""
   end point for update  specail  post  by its title using function save_post()
"""

@headless_controller.post('retrive/{title}')
def update_post(request ,datain : data_schema):
     save_post(datain.title,datain.content)
     return list_posts()
"""
   end point for delete  spiacal  post bt its tiltle  using function del_post() builded in utils.py
"""

@headless_controller.delete('retrive/{title}')
def delete_post(request,title:str):
     del_post(title)
     return list_posts()