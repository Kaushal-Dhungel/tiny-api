from Responses import JsonResponse
from Status import HTTP_200_OK
import json

def test_json_response():
    data = {'data':'okay'}
    response = JsonResponse(data,HTTP_200_OK)
    assert response.text == json.dumps(data)
    assert response.status_code == 200