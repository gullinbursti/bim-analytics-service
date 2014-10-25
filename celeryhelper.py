#! /usr/bin/env python

"""
Wrapper/helper script around the `celery` commandline tool.

Helps in making sure that the DJANGO_SETTINGS_MODULE, and
BIMANALYTICS_CONFIG_DIR environment variables are set correctly for
deveolopers.
"""

# -*- coding: utf-8 -*-

from celery.__main__ import main
import re
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


if __name__ == '__main__':
    configure_django_environment()
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
