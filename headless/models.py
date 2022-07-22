
from ninja import NinjaAPI, Schema


api=NinjaAPI()

class Post:
    title: str
    content: str


class PostIN(Schema):
    title: str
    content: str


class PostOut(Schema):
    first_name: str
    last_name: str
