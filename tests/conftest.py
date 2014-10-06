import django
import pytest


@pytest.fixture(scope="session")
def django_setup():
    django.setup()
