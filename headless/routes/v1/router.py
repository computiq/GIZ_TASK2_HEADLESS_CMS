from typing import List

from ninja import Router

from headless.schemas.messages import MsgSchema
from headless.schemas.post import PostOut, PostIn
from headless.utils import get_post, list_posts, del_post, save_post

router = Router(tags=['Posts'])


@router.get('/{title}', response={200: PostOut, 404: MsgSchema})
def read_post(request, title: str):
    """
    Read Post by its title then return it to the client.
    If it's Not found will return massage.
    """
    post = get_post(title)
    if not post:
        return 404, {'msg': 'Oops, post not found!'}
    return {'title': title, 'content': post}


@router.get('/', response={200: List[str]})
def read_all_posts(request):
    """
    Just return all the post we have as list of titles.
    In case that we don't have any post will return an empty list.
    """
    return list_posts()


@router.post('/', response={200: PostOut})
def create_post(request, payload: PostIn):
    """
    Create a new post then return it as schema.
    """
    save_post(payload.title, payload.content)
    return {'title': payload.title, 'content': payload.content}


@router.put('/{title}', response={200: MsgSchema})
def update_post(request, title: str, content: str):
    """
    Update an existing post by its title then return a massage.
    Here we're updating just the content.
    When given a title that is not existing will create a new post.
    """
    save_post(title, content)
    return {'msg': 'Post updated successfully'}


@router.delete('/{title}', response={200: MsgSchema, 404: MsgSchema})
def remove_post(request, title: str):
    """
    Delete an existing Post by its title then return a message.
    When given title is not found will return different massage.
    """
    result = del_post(title)
    if not result:
        return 404, {'msg': 'Opps!, there is no post with this title.'}
    return {'msg': 'Post deleted successfully'}
