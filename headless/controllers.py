from ninja import Router

account_controller = Router()

@account_controller.get('posts/')
   def ListPosts(request):
       return list_posts()

@account_controller.get('posts/{title}')
   def GetPost(request, title: str):
       return get_post(title)

@account_controller.put('posts/{title}')
    def UpdatePosts (request, title: str, content: str)
        return save_post(tilte, content.dict())

@account_controller.delete('posts/{title}')
    def DeletePost (request, title: str)
        return del_post(title)

#I'll take the L on this one :c