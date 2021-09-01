from api import Tinyapi
from webob import Response
api = Tinyapi()

def test_default_response():
    response = Response()
    api.default_response(response)
    assert response.text == "Not Found"
    assert response.status_code == 404
