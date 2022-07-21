from turtle import update
from ninja import Router
from headless import utils

end_points = Router()

@end_points.get('/list')
def list(request):
    return utils.list_posts()


@end_points.get('/retrieve/{title}')
def retrieve(request,title):
    return utils.get_post(title)


@end_points.post("create")
def create(request,title:str,content:str):
    utils.save_post(title,content)

 
@end_points.put("/update/{title}")
def update(request,title:str,content:str):
    utils.save_post(title,content)

   
@end_points.delete("/delete/{title}")
def delete(request,title:str):
    utils.del_post(title)


