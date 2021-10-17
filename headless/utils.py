import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_posts():
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    # returning list of dict contain all posts as title: content pair
    return list({re.sub(r"\.md$", "", filename): open(f"posts/{filename}").read()}
                for filename in filenames if filename.endswith(".md"))


def save_post(title, content):
    """
    Saves a blog post, given its title and Markdown
    content. If an existing post with the same title already exists,
    it is replaced.
    """
    filename = f"posts/{title}.md"
    """
    thinking about this we can create posts with the same title,content since 
    the id will be different  
    """
    default_storage.save(filename, ContentFile(content))


def get_post(title):
    """
    Retrieves a post by its title. If no such
    post exists, the function returns None.
    """
    try:
        with default_storage.open(f"posts/{title}.md") as f:
            return {title: f.read().decode("utf-8")}
    except FileNotFoundError:
        return error_response("Post Not Found", "you are trying to access removed or unexisting post")


def update_post(title: str, new_title: str, content: str):
    filename = f"posts/{title}.md"
    updated_file = f"posts/{new_title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        default_storage.save(updated_file, ContentFile(content))
    else:
        return error_response("seems like the post you want to update does not exist", "check if the post is already "
                                                                                   "there ,btw we have js_sucks so... XD")


def del_post(title: str):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    else:
        return error_response("post you are trying to delete does not exist", "ensure that the post title is correct")


def error_response(message, details):
    return {
        "message": message,
        "details": details
    }
