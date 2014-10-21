"""
Pytest global configuration information.

This file contains all session level filters.
"""

import django
import os


def pytest_configure(config):
    # pylint: disable=unused-argument
    """Configure Django environment variables for developers.

    Called after command line options have been parsed and all plugins and
    initial conftest files been loaded.  Reffer to the following for more
    information:

        http://pytest.org/latest/plugins.html#_pytest.hookspec.pytest_configure

    This hook:
        - Make certain that DJANGO_SETTINGS_MODULE, and BIMANALYTICS_CONFIG_DIR
          are set to sane defaults for developers.
        - Sets up Django, If this is not included, you will likely get an
          AppRegistryNotReady error while runing tests.

    Note that this function only sets the environment variables if they have
    not already been set, otherwise the original values stay in place.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bimanalytics.settings")
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault(
        'BIMANALYTICS_CONFIG_DIR',
        os.path.join(project_dir, 'tests-conf'))
    django.setup()
