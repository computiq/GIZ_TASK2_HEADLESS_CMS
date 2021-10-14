from ninja import Schema

class PostSchema(Schema):
    name: str
    content: str