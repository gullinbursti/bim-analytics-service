"""Dumby local_settings used by py.test."""

from __future__ import absolute_import
# ^^^ The above is required if you want to import from the celery
# library.  If you don't have this then `from celery.schedules import`
# becomes `proj.celery.schedules` in Python 2.x since it allows
# for relative imports by default.

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# -----------------------------------------------------------------------------
# Celery settings
BROKER_URL = None

# -----------------------------------------------------------------------------
# Django
SECRET_KEY = 'SECRET_KEY_ERROR_NEVER_USE_IN_PRODUCTION'

# -----------------------------------------------------------------------------
# Keen.io credentials
KEEN_IO_CREDENTIALS = {
    'project_id': None,
    'write_key': None,
    'read_key': None
}
