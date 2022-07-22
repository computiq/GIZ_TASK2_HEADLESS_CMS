from urllib import request
from . import utils

@controler.get('/user','/posts')
def list_posts():
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
    
@controler.get('/user','/posts','/title)
def get_post(title):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

@controler.post('/user','/create')

def save_post('title'):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

@controler.put('/user','/update')

def save_post('title'):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

@controler.delete('/user','/delete')
def del_post('title'):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
