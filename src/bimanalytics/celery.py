"""Celery service configuration."""

from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
import sys


# set the default Django settings module for the 'celery' program.
CONFIG_DIR = '/etc/bimanalytics'
SETTINGS_MODULE = 'bimanalytics.settings'


def setup_django_environment(settings_module, config_dir):
    """Django specific configuration.

    Sets up values for the DJANGO_SETTINGS_MODULE, BIMANALYTICS_CONFIG_DIR
    environment variables as well as update sys.path with the location for the
    local configuration.

    Note that Django bypasses the environment variables set by SetEnv.  So we
    are stuck having to maintain it here.  In the end it is not that bad, but
    makes this wsgi.py script platform specific.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    os.environ.setdefault('BIMANALYTICS_CONFIG_DIR', config_dir)
    sys.path.append(config_dir)

setup_django_environment(SETTINGS_MODULE, CONFIG_DIR)
# TODO - See if we can rename `app`
app = Celery('bimanalytics')  # pylint: disable=invalid-name

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    """
    A task that dumps its own request information.

    Used for debugging of course!
    """
    print('Request: {0!r}'.format(self.request))  # noqa pylint: disable=superfluous-parens
