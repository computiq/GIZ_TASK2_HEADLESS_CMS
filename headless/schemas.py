from ninja import Schema




class NotFound(Schema):
    detail : str



class PostsOut(Schema):
    title : str
    content : str

class PostsIn(Schema):
    title : str
    content : str
