import uuid


def generate_user_id():
    return str(uuid.uuid4())


def set_user_id_cookie(get_response):
    def middleware(request):
        if not request.COOKIES.get('user_id'):
            user_id = generate_user_id()
            response = get_response(request)
            response.set_cookie('user_id', user_id)
        else:
            response = get_response(request)
        return response
    return middleware

