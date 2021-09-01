from webob import request
from auth import  is_authenticated
from Requests import Request

def test_is_authenticated_without_token():
    res = is_authenticated(Request(environ={}))
    assert res == False

def test_is_authenticated_with_token():
    request = Request(environ={})
    request.bearer = '1234abcd'
    res = is_authenticated(request)
    assert res == False

    