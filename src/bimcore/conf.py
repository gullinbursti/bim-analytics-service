"""Configuration helpers."""

from __future__ import absolute_import
import os
import sys

__all__ = ('is_dev_environment',
           'get_local_conf_dir')


def is_dev_environment():
    """
    Return `True` if running in a deveopment environment.

    Defaults to `False`.

    Controlled via the `BIM_DEV` environment variable.  Please limit values to:
    `True` `False`.  Case insensitive.
    """
    raw_value = os.environ.get('BIM_DEV', False)
    value = None
    if not raw_value or raw_value.lower() in ('false', 'no', '0'):
        value = False
    elif raw_value.lower() in ('true', 'yes', '1'):
        value = True
    else:
        raise ValueError('BIM_DEV set to an invalid value')
    return value


def get_local_conf_dir(env_var, prod_conf_dir, project_dir=None):
    """
    Return the projects local configuration directory.

    Checks in the following order, first one wins:
        - Value in the environment variable specified by `env_var`.
        - If is_dev_environment() is False, returns `prod_conf_dir`.
        - If `project_dir` and `{project_dir}/conf` exists returns that value.
        - Returns `$CWD/conf`, if it exists.
        - If the durectory the script was launched from contains `/conf`,
          returns that.

    RuntimeError is thrown if:
        - It makes it through the previous list without finding anything.
        - The final directory does not exist.
    """
    cwd_conf = os.path.join(os.getcwd(), 'conf')
    exec_conf_dir = os.path.join(
        os.path.dirname(os.path.abspath(sys.argv[0])), 'conf')

    conf_dir = None
    if env_var in os.environ:
        conf_dir = os.environ[env_var]
    elif not is_dev_environment():
        conf_dir = prod_conf_dir
    elif project_dir:
        conf_dir = os.path.join(project_dir, 'conf')
    elif os.path.isdir(cwd_conf):
        conf_dir = cwd_conf
    elif os.path.isdir(exec_conf_dir):
        conf_dir = exec_conf_dir
    else:
        raise RuntimeError(
            'Unable to determine local configuration directory.')

    if not os.path.isdir(conf_dir):
        raise RuntimeError(
            'Local configuration directory \'{}\' does not '
            'exist.'.format(conf_dir))

    return conf_dir
