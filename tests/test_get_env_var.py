from tiny_api.get_env_var import get_env_vars

def test_get_env_vars():
    data = get_env_vars('abcdefg',default='hello')
    assert data == 'hello'