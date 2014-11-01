"""Globaly configure Keen IO library credentials."""

from __future__ import absolute_import
from django.conf import settings
import keen as keenio

try:
    keenio.project_id = settings.KEEN_IO_CREDENTIALS['project_id']
    keenio.write_key = settings.KEEN_IO_CREDENTIALS['write_key']
    keenio.read_key = settings.KEEN_IO_CREDENTIALS['read_key']
except AttributeError as original:
    raise RuntimeError(
        original,
        'Looks like KEEN_IO_CREDENTIALS was not set in \'local_settings\'.')
