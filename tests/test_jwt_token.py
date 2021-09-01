from jwt_token import create_access_token,decode_access_token, create_refresh_token
import uuid

def test_create_decode_token():
    user_id = 1
    username = "hellouser"
    seconds = 1800
    secret_key = 'mysecretkey'

    token = create_access_token(user_id,username,seconds,secret_key)

    is_valid,data = decode_access_token(token,secret_key)

    assert is_valid == True
    assert data['id'] == user_id
    assert data['username'] == username


def test_create_refresh_token():
    refresh_token = create_refresh_token()
    assert type(refresh_token) == uuid.UUID