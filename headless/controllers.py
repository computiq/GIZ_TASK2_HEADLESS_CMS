from ninja import NinjaAPI
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import re

api = NinjaAPI()


@api.get("/posts")
def getAllPost(request):
    _, filenames = default_storage.listdir("posts")
    return list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if filename.endswith(".md")))


@api.post("/posts")
def storePost(request, title: str, content: str):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    return {"state": "Success", "message": "Post Added Successfully"}


@api.get("/post/{title}")
def getPost(request, title: str):
    try:
        f = default_storage.open(f"posts/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return {"state": "error", "message": title + "  not exist"}

@api.put("/posts/{title}")
def editPost(request, title: str, content: str):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        default_storage.save(filename, ContentFile(content))
        return {"state": "Success", "message": "Post Edited Successfully"}
    else:
        return {"state": "error", "message": title + "  not exist"}


@api.delete('/post/{title}')
def deletePost(request, title: str):
    filename = f"posts/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        return {"state": "Success", "message": "Post Deleted Successfully"}
    else:
        return {"state": "error", "message": title + "  not exist"}