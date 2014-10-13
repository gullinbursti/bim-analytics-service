"""Unit tests for the Selfieclub event endpoint device serializers."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
from decimal import Decimal
from io import StringIO
from mock import patch
from rest_framework.parsers import JSONParser
from selfieclub.serializers import DeviceSerializer
import pytest


RESOLUTION_VALUES_GOOD = (20, 1024*10)
RESOLUTION_VALUES_BAD = (None, '', 0, -100, 19, 1024*10+1, 'some_string')


@pytest.fixture(scope='function')
def device_test_data():
    # pylint: disable=function-redefined, global-variable-undefined
    # pylint: disable=invalid-name, unnecessary-lambda, redefined-outer-name
    """Return a copy of device test data.

    This function uses closures, and redefines itself for efficency.  I am
    also doing a bit of experimentation.
    """
    stream = StringIO(DEVICE_GOOD_JSON)
    data = JSONParser().parse(stream)
    global device_test_data
    device_test_data = lambda: data.copy()
    return data


@pytest.mark.usefixtures("django_setup")
class TestDeviceDeserialization(object):
    # pylint: disable=no-self-use, no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg, redefined-outer-name
    # pylint: disable=too-few-public-methods

    """Testing the Deserialization with MemberSerializer."""

    @pytest.mark.parametrize(
        ('field_name', 'validator'),
        [('adid', 'selfieclub.serializers.validate_device_adid'),
         ('cpu', 'selfieclub.serializers.validate_device_cpu'),
         ('density', 'selfieclub.serializers.validate_device_density'),
         ('hardware_make',
          'selfieclub.serializers.validate_device_hardware_make'),
         ('hardware_model',
          'selfieclub.serializers.validate_device_hardware_model'),
         ('locale', 'selfieclub.serializers.validate_device_locale'),
         ('orientation', 'selfieclub.serializers.validate_device_orientation'),
         ('orientation_deg',
          'selfieclub.serializers.validate_device_orientation_deg'),
         ('os', 'selfieclub.serializers.validate_device_os'),
         ('os_version', 'selfieclub.serializers.validate_device_os_version'),
         ('time', 'selfieclub.serializers.validate_device_time'),
         ('token', 'selfieclub.serializers.validate_device_token'),
         ('tz', 'selfieclub.serializers.validate_device_tz'),
         ('user_agent', 'selfieclub.serializers.validate_device_user_agent')])
    def test_calls_validator(self, device_test_data, field_name, validator):
        """Make sure that the proper validator has been called.

        Also makes certain that the the ValidationError() exception is being
        listened to.
        """
        with patch(validator) as patched:
            patched.side_effect = ValidationError(
                'Fake validation error in unit testing.', 'boo')
            serializer = DeviceSerializer(data=device_test_data)
            assert not serializer.is_valid()
            assert serializer.errors
            patched.assert_called_with(device_test_data[field_name])
            assert not set([field_name]) - set(serializer.errors.keys())


# -----------------------------------------------------------------------------
# resolution_x & resolution_y
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", RESOLUTION_VALUES_GOOD)
def test_validate_resolution_y_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['resolution_y'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.resolution_y


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", RESOLUTION_VALUES_BAD)
def test_validate_resolution_y_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['resolution_y'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['resolution_y']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", RESOLUTION_VALUES_GOOD)
def test_validate_resolution_x_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['resolution_x'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.resolution_x


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", RESOLUTION_VALUES_BAD)
def test_validate_resolution_x_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['resolution_x'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['resolution_x']) - set(serializer.errors.keys())


# -----------------------------------------------------------------------------
# battery_per
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", [None, '', -1, -0.00001, 100.000001, 'hello'])
def test_validate_battery_per_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['battery_per'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['battery_per']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", [Decimal(0), Decimal(100), Decimal(0.00000), Decimal(100.00000),
              Decimal(34.0980)])
def test_validate_battery_per_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['battery_per'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.battery_per


DEVICE_GOOD_JSON = u"""
{
    "adid": "TODO - fix adid",
    "battery_per": 57.6789,
    "cpu": "TODO - fix cpu",
    "density": "TODO - fix density",
    "hardware_make": "TODO - fix hardware_make",
    "hardware_model": "TODO - fix hardware_model",
    "locale": "TODO - fix locale",
    "orientation": "TODO - fix orientation",
    "orientation_deg": "TODO - fix orientation_deg",
    "os": "TODO - fix os",
    "os_version": "TODO - fix os_version",
    "resolution_x": 768,
    "resolution_y": 1024,
    "time": "TODO - fix time",
    "token": "TODO - fix token",
    "tz": "TODO - fix tz",
    "user_agent": "TODO - fix user_agent"
}
"""
