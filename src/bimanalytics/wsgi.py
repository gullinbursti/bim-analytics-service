"""
Apache WSGI config for bimanalytics project.

NOTE: This script is platform/deployment specific.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

VIRTUALENV_DIR = '/opt/built-in-menlo/bimanalytics'
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


def activate_virtualenv(virtualenv_dir):
    """Activate virtualenv."""
    activate_this = os.path.join(virtualenv_dir, 'bin', 'activate_this.py')
    exec(  # pylint: disable=exec-used
        compile(open(activate_this).read(), activate_this, 'exec'),
        dict(__file__=activate_this))

setup_django_environment(SETTINGS_MODULE, CONFIG_DIR)
activate_virtualenv(VIRTUALENV_DIR)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()  # noqa - required by WSGI.  pylint: disable=invalid-name
