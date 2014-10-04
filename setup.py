from os import path
from setuptools import setup

setup(
    name='bim-analytic-service',
    # Please read the following for setting the version number:
    #    - https://pythonhosted.org/setuptools/setuptools.html#specifying-your-project-s-version  # noqa
    version='0.0.0-dev',
    author='Pedro H <pedro@builtinmenlo.com>, Phillip Winn <phillip@builtinmenlo.com>',
    author_email='pedro@builtinmenlo.com',
    install_requires=[
        'Django>=1.6.5',
        'amqp>=1.4.5',
        'celery>=3.1.13',
        'djangorestframework>=2.3.14',
        'drf-compound-fields>=0.2.1',
        'requests>=2.4.1'])
