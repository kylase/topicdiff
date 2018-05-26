import pytest

from flask import url_for

def test_home_page(client):
    assert client.get(url_for('index')).status_code == 200

def test_not_found(client):
    assert client.get('/not-a-valid-page').status_code == 404