import re

from ninja import  Schema
from typing import List
from pydantic import validator
class PostSchema(Schema):
    title: str
    body: str


    @validator("title")
    def validate_title(cls, value):
        if re.match(r"^[^\w\s]", value):
            raise ValueError("Start Title With special Chars is not Valid !")
        if(61 > len(value) > 1):
           return value.strip()
        raise ValueError("Title Length must be in range 2-60 Chars")

    @validator("body")
    def validate_body(cls, value):
        if(251 > len(value) > 1):
            return value.strip()
        raise ValueError("Body Length must be in range 2-250 Chars")



class ResponseSchema(Schema):
    status: bool
    data: List[dict]
    message: str