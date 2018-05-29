import pytest

def test_compare_valid_content(client):
    data = {
        'content': ['Content One', 'Content Two']
    }

    assert client.post('/api/documents/compare', json=data).status_code == 200

def test_compare_no_content(client):
    data = {
        'content': []
    }

    assert client.post('/api/documents/compare', json=data).status_code == 400

def test_compare_invalid_model(client):
    data = {
        'content': ['Content One', 'Content Two'],
        'model': 'other'
    }

    assert client.post('/api/documents/compare', json=data).status_code == 400