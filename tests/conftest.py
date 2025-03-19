import pytest

from app.core.container import Container
from app.main import app
from fastapi.testclient import TestClient
from dependency_injector.providers import Factory

from tests.mocks.transaction import MockTransactionService
from tests.mocks.user import MockUserService


@pytest.fixture
def client():
    container = Container()
    container.user_service.override(Factory(MockUserService))
    container.transaction_service.override(Factory(MockTransactionService))
    
    app.dependency_overrides[Container.user_service] = container.user_service
    app.dependency_overrides[Container.transaction_service] = container.transaction_service

    with TestClient(app) as c:
        yield c