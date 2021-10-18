from django.http.response import JsonResponse
from ninja import Schema

class PostSchema(Schema):
    name: str
    content: str
