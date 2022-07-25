from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/path")
def get_operation(request):
    return {"get"}


@api.post("/path")
def post_operation(request):
    return {"post"}


@api.put("/path")
def put_operation(request):
    return {"put"}


@api.delete("/path")
def delete_operation(request):
    return {"delete"}
