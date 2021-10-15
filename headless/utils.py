import string , re , frontmatter , random

from datetime import datetime
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.paginator import Paginator

def list_posts():
    """
    Returns a list of all names of blog posts.
    """
    _, filenames = default_storage.listdir("posts")
    return list((get_post(re.sub(r"\.md$", "", filename))
                for filename in filenames if filename.endswith(".md")))


def save_post(title, body, update = False, slug = ""):
    """
    Saves a blog post, given its title , slug and Markdown
    content. If an existing post with the same slug already exists,
    Return None

    also Update blog post, given its title and Markdown
    content. If not existing post with the same slug,
    Return None
    """
    if update:
        filename = get_filename(slug)
        if  default_storage.exists(filename):
            post = get_post(slug)
            content = generate_metadata(title= title, slug=post['slug'], published_at= post['published_at'], updated_at= datetime.now(), content= body)
            default_storage.delete(filename)
            default_storage.save(filename, ContentFile(content))
        else:
            return None

    else:
        slug = generate_slug(title)
        filename = get_filename(slug)
        if default_storage.exists(filename):
            random_str = ''.join(random.choice(string.ascii_lowercase + " " + string.digits) for _ in range(25))
            slug = generate_slug(random_str)
            filename = get_filename(slug)
        content = generate_metadata(title= title, slug=slug, published_at= datetime.now(), updated_at= datetime.now(), content= body)
        default_storage.save(filename, ContentFile(content))

    return get_post(slug)

def get_post(slug):
    """
    Retrieves a post by its slug. If no such
    post exists, the function returns None.
    """
    try:
        f = frontmatter.loads(default_storage.open(get_filename(slug)).read().decode("utf-8"))
        return {"title": f['title'], "slug": f['slug'], "body":f.content, "published_at": f['published_at'], "updated_at":f['updated_at'] }
    except FileNotFoundError:
        return None

def del_post(slug):
    """
    Delete a post by its slug. If no such
    post exists, the function returns None.
    """
    filename = get_filename(slug)
    if default_storage.exists(filename):
        post = get_post(slug)
        default_storage.delete(filename)
        return post
    return None



def get_filename(slug):
    """
    return relative path for give file name
    """
    return f"posts/{slug}.md"
def generate_slug(string):
    return re.sub(r"\s+", "-", string)
def generate_metadata(**metadata):
    """
    Generate and return Metadata for (Created, Updated) Post
    """
    return f'---\ntitle: {metadata["title"]}\nslug: {metadata["slug"]}\npublished_at: {metadata["published_at"]}\nupdated_at: {metadata["updated_at"]}\n---\n{metadata["content"]}'

def response(status, msg, data=[], paginate:bool = False, per_page:int = 10, page_num: int = 1):
    """
    Helper Function that return Pagination Data
    or
    Return ResponseSchema
    """
    if paginate:
        pagination = Paginator(data, per_page)
        try:
            p = pagination.page(page_num)
        except:
            return 404,{"status":False, "message":"Page Not Found", "data":[]}
        data =  [{
            'total_count': len(data),
            'per_page': per_page,
            'from_record': p.start_index(),
            'to_record': p.end_index(),
            'previous_page': p.previous_page_number() if p.has_previous() else None,
            'current_page': p.number,
            'next_page': p.next_page_number() if p.has_next() else None,
            'page_count': pagination.num_pages,
            'count' : len(p.object_list),
            'data': p.object_list,
        }]
    return {"status":status, "message":msg, "data":data}