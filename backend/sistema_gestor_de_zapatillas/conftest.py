import pytest

from sistema_gestor_de_zapatillas.users.models import User
from sistema_gestor_de_zapatillas.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
