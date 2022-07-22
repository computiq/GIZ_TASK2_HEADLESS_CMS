from turtle import title
from datetime import date
from typing import List
from django.shortcuts import get_object_or_404

from headless.models import PostIN, PostOut, Post
from headless.utils import *
from ninja import Router

mRouter = Router()




@mRouter.post("/create a new post")
def create_post(request, payload: PostIN):
    post = Post.objects.create(**payload.dict())
    return {"title": post.title}

@mRouter.get(f"/Retrieves a post/{title()}", response=PostOut)
def get_post(request, title: str):
    post = get_object_or_404(Post, title)
    return post

@mRouter.get("/Returns all posts", response=List[PostOut])
def list_post(request):
    qs = Post.objects.all()
    return qs

@mRouter.put(f"/update a post/{title()}")
def update_post(request, title: str, payload: PostIN):
    post = get_object_or_404(Post, title)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return {"success": True}


@mRouter.delete(f"/delete a certain post/{title()}")
def delete_employee(request, title: str):
    post = get_object_or_404(Post, title)
    post.delete()
    return {"success": True}
