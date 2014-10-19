#!/usr/bin/env python

"""Django management script."""

import os
import sys


def configure_django_environment():
    """
    Set BIMANALYTICS_CONFIG_DIR environment variable, if not already set.

    Make certain that DJANGO_SETTINGS_MODULE, and BIMANALYTICS_CONFIG_DIR are
    set to sane defaults for developers.

    Note that this function only sets the environment variables if they have
    not already been set, otherwise the original values stay in place.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bimanalytics.settings")
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.environ.setdefault(
        "BIMANALYTICS_CONFIG_DIR",
        os.path.join(project_dir, 'conf'))


if __name__ == "__main__":
    configure_django_environment()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
