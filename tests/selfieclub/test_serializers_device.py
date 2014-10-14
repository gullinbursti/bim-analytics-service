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
PERCENTAGE_VALUES_GOOD = (Decimal(0), Decimal(100), Decimal(0.00000),
                          Decimal(100.00000), Decimal(34.0980))
PERCENTAGE_VALUES_BAD = (None, '', -1, -0.00001, 100.000001, 'hello')


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
        [('adid', 'selfieclub.serializers.validate_guid'),
         ('locale', 'selfieclub.serializers.validate_device_locale'),
         ('time', 'selfieclub.serializers.validate_device_time'),
         ('token', 'selfieclub.serializers.validate_device_token'),
         ('tz', 'selfieclub.serializers.validate_device_tz')])
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
@pytest.mark.parametrize("value", PERCENTAGE_VALUES_BAD)
def test_validate_battery_per_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['battery_per'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['battery_per']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", PERCENTAGE_VALUES_GOOD)
def test_validate_battery_per_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['battery_per'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.battery_per


# -----------------------------------------------------------------------------
# cpu
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", PERCENTAGE_VALUES_BAD)
def test_validate_cpu_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['cpu'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['cpu']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", PERCENTAGE_VALUES_GOOD)
def test_validate_cpu_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['cpu'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.cpu


# -----------------------------------------------------------------------------
# pixel_density
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", (None, '', 0, -1, 1024*10+1, 'some_string'))
def test_validate_pixel_density_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['pixel_density'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['pixel_density']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", (1, 1024*10))
def test_validate_pixel_density_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['pixel_density'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.pixel_density


# -----------------------------------------------------------------------------
# os
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", (None, '', '\t', '\niOS', 'Ios', ' ios', ' ios  ', 'a'*9,
              'Android', 'android '))
def test_validate_os_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['os'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['os']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", ('ios', 'android'))
def test_validate_os_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['os'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.os_


# -----------------------------------------------------------------------------
# hardware_make
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", (None, '', 'y', 'z'*65, 'Apple   ', ' Apple', ' Samsung '))
def test_validate_hardware_make_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['hardware_make'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['hardware_make']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", ('HTC', 'Samsung', 'Apple', 'AB', 'a'*64))
def test_validate_hardware_make_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['hardware_make'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.hardware_make


# -----------------------------------------------------------------------------
# hardware_model
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", (None, '', 'y', 't'*65, '\niPhone 5 ', ' iPhone 5', '\tiPhone 5',
              'a'))
def test_validate_hardware_model_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['hardware_model'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['hardware_model']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", ('iPhone 5', 'iPhone 6plus', 'Galaxy S', 'Galaxy S II',
              'Galaxy S5', 'GT-I9300', 'gH', 'r'*64))
def test_validate_hardware_model_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['hardware_model'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.hardware_model


# -----------------------------------------------------------------------------
# os_version
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", (None, '', 'g', '   8.0.2', '8.0.2\n', 'r'*33))
def test_validate_os_version_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['os_version'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['os_version']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", ('8.0.2', '7.1.1', '7.1', '2.3.7', '4.4.4', '1.1', 'b'*32))
def test_validate_os_version_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['os_version'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.os_version


# -----------------------------------------------------------------------------
# orientation
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", (None, '', '\nportrait', 'portrait\r', 'portrait   ',
              'Landscape'))
def test_validate_orientation_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['orientation'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['orientation']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", ('landscape', 'portrait'))
def test_validate_orientation_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['orientation'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.orientation


# -----------------------------------------------------------------------------
# orientation_deg
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", (None, '', -1, 91, 'some_string'))
def test_validate_orientation_deg_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['orientation_deg'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['orientation_deg']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", (0, 90, 180, 270))
def test_validate_orientation_deg_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['orientation_deg'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.orientation_deg


# -----------------------------------------------------------------------------
# user_agent
# -----------------------------------------------------------------------------
@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize("value", ('g'*2049, 'Apple-iPhone2C1/901.334 ',
                                   '\nApple-iPhone2C1/901.334'))
def test_validate_user_agent_with_bad_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['user_agent'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set(['user_agent']) - set(serializer.errors.keys())


@pytest.mark.usefixtures("django_setup")
@pytest.mark.parametrize(
    "value", (
        '',
        'Apple-iPhone2C1/901.334',
        'Apple-iPhone5C2/1001.525',
        'Apple-iPod5C1/1001.523',
        'Apple-iPad2C3/1001.403',
        'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',  # noqa
        'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',  # noqa
        'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',  # noqa
        'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',  # noqa
        'a'*2048))
def test_validate_user_agent_with_good_values(device_test_data, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['user_agent'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.user_agent


@pytest.mark.usefixtures("django_setup")
def test_validate_user_agent_none(device_test_data):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """TODO - add something."""
    device_test_data['user_agent'] = None
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert '' == serializer.object.user_agent


DEVICE_GOOD_JSON = u"""
{
    "adid": "558D52FD-8B0A-4850-ADF4-FBC522D29F39",
    "battery_per": 57.6789,
    "cpu": 93.19216,
    "pixel_density": 157,
    "hardware_make": "Apple",
    "hardware_model": "iPhone 4s",
    "locale": "TODO - fix locale",
    "orientation": "portrait",
    "orientation_deg": 0,
    "os": "ios",
    "os_version": "7.1.2",
    "resolution_x": 768,
    "resolution_y": 1024,
    "time": "TODO - fix time",
    "token": "TODO - fix token",
    "tz": "TODO - fix tz",
    "user_agent": "Apple-iPhone5C2/1001.525"
}
"""
