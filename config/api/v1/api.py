from ninja import NinjaAPI

from headless.routes.v1.router import router as post_router_v1

"""
API V1.X.X
"""

api = NinjaAPI(version='1.0.0', title='Computiq Blog API', description='Simple Blog API')

api.add_router('/posts', post_router_v1)
