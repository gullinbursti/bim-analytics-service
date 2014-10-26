"""
Apache WSGI config for bimanalytics project.

NOTE: This script is platform/deployment specific.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

VIRTUALENV_DIR = '/opt/built-in-menlo/bimanalytics'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bimanalytics.settings')


def activate_virtualenv(virtualenv_dir):
    """Activate virtualenv."""
    activate_this = os.path.join(virtualenv_dir, 'bin', 'activate_this.py')
    exec(  # pylint: disable=exec-used
        compile(open(activate_this).read(), activate_this, 'exec'),
        dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()  # noqa - required by WSGI.  pylint: disable=invalid-name
