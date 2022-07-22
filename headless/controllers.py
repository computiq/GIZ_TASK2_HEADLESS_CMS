from ninja import Router
from headless.utils import *

posts_controller = Router()


@posts_controller.get('posts')
def list_posts(request):
    """
    Returns a list of all titles of the psots.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if filename.endswith(".md")))


@posts_controller.get('posts/title')
def get_post(request, title):
    """
    To retrieve a certain post using the title.
    """
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


@posts_controller.put('update')
def save_post(request, title, content):
    """
    Creates a new post.If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


@posts_controller.post('create')
def save_post(request, title, content):
    """
    to update a certain post... given the title
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


@posts_controller.delete('delete')
def del_post(request, title):
    """
    Delete a blog post after you give it the title.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        default_storage.delete(ContentFile())

    default_storage.save(filename, ContentFile())