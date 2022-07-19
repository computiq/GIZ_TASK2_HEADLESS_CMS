from headless.utils import *
from ninja import Router

CMS_app = Router()

# to list all posts
@CMS_app.get('ListAllPosts')
def list_posts(request):
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


# to retrieve a certain post
@CMS_app.get('RetrieveOnePost')
def get_post(request, title):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


# to create a new post
@CMS_app.post('CreateNewPost')
def save_post(request, title, content):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


# to update a certain post
@CMS_app.put('Update')
def update_post(request, title, content):
    filename = f"posts/{title}.md"

    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

    
# to delete a certain post
@CMS_app.delete('Delete')
def del_post(request, title):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        

