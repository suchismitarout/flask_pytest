import pytest

from app import app as flask_app


@pytest.fixture
def app():
    """
        it'll initialize flask_app
    """
    yield flask_app


@pytest.fixture
def client(app):
    """
        it'll start a demo server for flask_app
    """
    return app.test_client()