from ninja import Router

router = Router(tags=['Posts'])


@router.get('/{id}')
def read_post(request, ):
    pass


def read_all_posts(request, ):
    pass


def update_post(request, ):
    pass


def remove_post(request, ):
    pass
