from ninja import ModelSchema

from headless.models import Post


class PostIn(ModelSchema):
    class Config:
        model = Post
        model_fields = ['title', 'content']


class PostOut(ModelSchema):
    class Config:
        model = Post
        model_fields = ['title', 'content']
