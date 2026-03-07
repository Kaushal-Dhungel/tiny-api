from tiny_api.auth import is_authenticated
from tiny_api.Requests import Request
from tiny_api.middleware import Middleware
from tiny_api.jwt_token import create_access_token

def test_is_authenticated_without_token():
    res = is_authenticated(Request(environ={}))
    assert res == False

def test_is_authenticated_with_token():
    request = Request(environ={})
    request.bearer = '1234abcd'
    res = is_authenticated(request)
    assert res == False


def test_request_has_is_authenticated_attribute():
    request = Request(environ={})
    assert request.is_authenticated == False


def test_middleware_marks_valid_bearer_authenticated():
    middleware = Middleware(app=None)
    token = create_access_token(user_id=1, username='user', seconds=1800)
    request = Request.blank('/', headers={'Authorization': f'Bearer {token}'})
    request = middleware.tweak_request(request)
    assert request.is_authenticated == True

    
