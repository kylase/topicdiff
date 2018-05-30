import pytest

def test_swagger(client):
    assert client.get('/api/swagger.json').status_code == 200

def test_api_documentation(client):
    assert client.get('/api/docs').status_code == 301
