import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from ninja import Router


router = Router()


@router.get('/view-all')
def list_posts(request):
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


@router.post('/create')
def save_post(request, title: str, content: str):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    return "New File was created successfully"


@router.get('/get-one-post/{title}')
def get_post(request, title: str):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None.
    """
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return f"posts/{title}.md does not exist"


@router.put('/update/{title}')
def update_post(request, title: str, new_content: str):
    filename = f"posts/{title}.md"

    if default_storage.exists(filename):
        default_storage.delete(filename)
        default_storage.save(filename, ContentFile(new_content))
        return f"The file {filename} was updated"
    else:
        return f"{filename} does not exist"


@router.delete('/delete/{title}')
def del_post(request, title: str):
    filename = f"posts/{title}.md"

    if default_storage.exists(filename):
        default_storage.delete(filename)
        return f"{title} File was deleted"
    else:
        return f"{filename} does not exist"
