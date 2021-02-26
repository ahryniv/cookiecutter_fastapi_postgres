import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.conf.settings import Settings
from {{cookiecutter.project_slug}}.database import metadata


@pytest.fixture(scope='session')
def app() -> 'FastAPI':
    test_settings = Settings()
    app = create_app(test_settings)
    metadata.create_all()
    return app


@pytest.fixture(scope='session')
def client(app: FastAPI) -> TestClient:
    client_ = TestClient(app, raise_server_exceptions=False)
    return client_
