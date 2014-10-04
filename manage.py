#!/usr/bin/env python
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_DIR = os.path.join(os.path.dirname(BASE_DIR), 'bimanalytics-config')
sys.path.append(CONFIG_DIR)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bimanalytics.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
