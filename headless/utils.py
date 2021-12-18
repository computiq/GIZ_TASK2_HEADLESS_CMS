import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_posts():
   
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
def save_post(title, content):
    
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)

    default_storage.save(filename, ContentFile(content))



def del_post(title):
    pass 
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        return "delete