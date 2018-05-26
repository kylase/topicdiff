import pytest
from app import create_app
from app.settings import TestConfig

@pytest.fixture
def app():
    _app = create_app(TestConfig)
    return _app