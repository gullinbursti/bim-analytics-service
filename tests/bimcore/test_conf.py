"""Test bimcore.conf."""

from __future__ import absolute_import
from mock import patch
import bimcore.conf as bimconf
import os
import sys
import pytest


# -----------------------------------------------------------------------------
# is_dev_environment()
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('value', ['true', 'True', 'TRUE', 'trUE', 'yes', '1'])
def test_is_dev_environment_on_true(value):
    """Test with truethy values."""
    with patch.dict('os.environ', {'BIM_DEV': value}):
        assert bimconf.is_dev_environment()


@pytest.mark.parametrize(
    'value', ['false', 'False', 'FALSE', 'faLsE', 'no', '0', ''])
def test_is_dev_environment_on_false(value):
    """Test with falsey values."""
    with patch.dict('os.environ', {'BIM_DEV': value}):
        assert not bimconf.is_dev_environment()


@pytest.mark.parametrize(
    'value', ['jsdofiu', '-1', '2', 'OK', 'ok'])
def test_is_dev_environment_bad_values(value):
    """Test with falsey values."""
    with patch.dict('os.environ', {'BIM_DEV': value}), \
            pytest.raises(ValueError):
        bimconf.is_dev_environment()


def test_is_dev_environment_defaults_to_false():
    """Make sure `False1 by default."""
    with patch.dict('os.environ', clear=True):
        assert not bimconf.is_dev_environment()


# -----------------------------------------------------------------------------
# get_local_conf_dir()
# -----------------------------------------------------------------------------
def test_get_local_conf_dir_env_var_wins():
    """Make sure that the environment variable always wins."""
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    env_dir = '/env/conf/dir/here'
    environ = {env_var: env_dir}
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.return_value = True
        assert env_dir == bimconf.get_local_conf_dir(
            env_var=env_var, prod_conf_dir=prod_conf_dir)
        isdir.assert_called_once_with(env_dir)


def test_get_local_conf_dir_is_not_dev_wins():
    """
    Make sure that prod_conf_dir is sent back when in production.

    The switch between 'dev' and 'prod' is managed through the 'BIM_DEV'
    environment variable.
    """
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    environ = {'BIM_DEV': 'False'}
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.return_value = True
        assert prod_conf_dir == bimconf.get_local_conf_dir(
            env_var=env_var, prod_conf_dir=prod_conf_dir)
        isdir.assert_called_once_with(prod_conf_dir)


def test_get_local_conf_dir_is_dev_proj_dir_wins():
    """Suplied project directory, if given."""
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    proj_dir = '/home/foo/fake/bar'
    proj_conf_dir = '/home/foo/fake/bar/conf'
    environ = {'BIM_DEV': 'True'}
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.return_value = True
        assert proj_conf_dir == bimconf.get_local_conf_dir(
            env_var=env_var, prod_conf_dir=prod_conf_dir, project_dir=proj_dir)
        isdir.assert_called_once_with(proj_conf_dir)


def test_get_local_conf_dir_is_not_dev_cwd_wins():
    """Configuration directory relative to CWD when in dev mode."""
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    environ = {'BIM_DEV': 'True'}
    cwd_conf_dir = os.path.join(os.getcwd(), 'conf')
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.return_value = True
        assert cwd_conf_dir == bimconf.get_local_conf_dir(
            env_var=env_var, prod_conf_dir=prod_conf_dir)
        isdir.assert_called_with(cwd_conf_dir)


def test_get_local_conf_dir_is_not_dev_exec_dir_wins():
    """Configuration relative to calling script's location."""
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    environ = {'BIM_DEV': 'True'}
    exec_conf_dir = os.path.join(
        os.path.dirname(os.path.abspath(sys.argv[0])), 'conf')
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.side_effect = lambda x: x == exec_conf_dir
        assert exec_conf_dir == bimconf.get_local_conf_dir(
            env_var=env_var, prod_conf_dir=prod_conf_dir)
        isdir.assert_called_with(exec_conf_dir)


def test_get_local_conf_dir_nothing_wins_exception():
    """Exception when none of the rules match."""
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    environ = {'BIM_DEV': 'True'}
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.return_value = False
        exception = pytest.raises(
            RuntimeError,
            bimconf.get_local_conf_dir,
            env_var=env_var,
            prod_conf_dir=prod_conf_dir)
        assert 'Unable to determine local configuration directory.' \
            in repr(exception.value)


def test_get_local_conf_dir_env_dir_not_exist_exception():
    """Exception if selected target directory does not exist."""
    env_var = 'SOME_CONF_DIR'
    prod_conf_dir = '/etc/something/fake'
    env_dir = '/env/conf/dir/here'
    environ = {env_var: env_dir}
    with patch.dict('os.environ', values=environ, clear=True), \
            patch('os.path.isdir') as isdir:
        isdir.return_value = False
        exception = pytest.raises(
            RuntimeError,
            bimconf.get_local_conf_dir,
            env_var=env_var,
            prod_conf_dir=prod_conf_dir)
        assert 'Local configuration directory' \
            in repr(exception.value)
