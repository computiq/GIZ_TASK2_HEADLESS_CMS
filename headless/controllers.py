import re
from os import read
from ninja import Router,Schema
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

headless_controllers = Router()

class DataSchema(Schema):
    title: str
    content : str

'''class put(Schema):
    title:str'''

@headless_controllers.get('list')
def list_posts(request):
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


@headless_controllers.get('{index}')
def list_posts(request,index :int):
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

@headless_controllers.post('')
def save_post(request,title, content, data_in:DataSchema):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

@headless_controllers.put('{index}')
def get_post(request,title,index:str,payload: DataSchema):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

@headless_controllers.delete('{index}')
def delete_data(request,index:int):
       default_storage = (index)