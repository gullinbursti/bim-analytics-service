"""
Pytest global configuration information.

This file contains all session level filters.
"""

import django
import pytest


@pytest.fixture(scope="session")
def django_setup():
    """
    All unint tests that use Django REST must include this fixture.

    If this fixture is not included, you will likely get an
    AppRegistryNotReady error while runing tests.
    """
    django.setup()
