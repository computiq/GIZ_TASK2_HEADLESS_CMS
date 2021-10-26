from ninja import Router, Schema
from django.http import JsonResponse

from headless.utils import del_post, get_post, list_posts, save_post

headless_controlear = Router()

# you have to CRUD (Create, Read, Update, and Delete) blog posts
"""
'posts' directory: save/update and create posts, 
Each file is a markdown file where the filename is the title of the post and the file content is the content of the post.
Each file represents a single post.
A sample of two files (two blog posts) are there for your reference.
"""

# make Schema 
class DataSchema(Schema):
    title : str
    content : str

DataSchema.update_forward_refs()


# list all posts
# GET /posts

@headless_controlear.get('posts')
def all_posts(request):
    return JsonResponse( {"All Posts" : list_posts()} )


# retrieve a certain post
# GET /posts/{title}

@headless_controlear.get('posts/{title}')
def retrive_post(request, title : str):
    return JsonResponse( {f"{title}" : get_post(title)} )


# create a new post
# POST /posts

@headless_controlear.post("posts")
def create_post(request, data_in : DataSchema):
    title = data_in.title
    content = data_in.content
    save_post(title, content)
    return JsonResponse( {"title" : f"{title}", "content" : f"{content}"} )


# update a certain post
# PUT /posts/{title}

@headless_controlear.put('posts/{title}')
def update_post(request, title : str, content : str):
    save_post(title, content)
    return JsonResponse( {"title saved" : f"{title}", "content saved" : f"{content}"} )


# delete a certain post
# DELETE /posts/{title}

@headless_controlear.delete('posts/{title}')
def delete_post(request, title : str):
    del_post(title)
    return JsonResponse( {f"post Deleted Succesfully" : f"{title}"} )