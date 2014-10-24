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


def get_device_test_data():
    """Return a copy of device test data."""
    stream = StringIO(DEVICE_GOOD_JSON)
    return JSONParser().parse(stream)


class TestDeviceDeserialization(object):
    # pylint: disable=no-self-use, no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg, redefined-outer-name
    # pylint: disable=too-few-public-methods

    """Testing the Deserialization with MemberSerializer."""

    # TODO: get rid of this, and actually perform direct tesing.  Do not
    # assume that the serializer is calling the correct methods.  It could
    # easily be calling something else.
    @pytest.mark.parametrize(
        ('field_name', 'validator'),
        [('adid', 'selfieclub.serializers.validate_guid'),
         ('locale', 'selfieclub.serializers.validate_locale_code'),
         ('time', 'selfieclub.serializers.validate_utc_iso8601'),
         ('tz', 'selfieclub.serializers.validate_utc_offset')])
    def test_calls_validator(self, field_name, validator):
        """Make sure that the proper validator has been called.

        Also makes certain that the the ValidationError() exception is being
        listened to.
        """
        device_test_data = get_device_test_data()
        with patch(validator) as patched:
            patched.side_effect = ValidationError(
                'Fake validation error in unit testing.', 'boo')
            serializer = DeviceSerializer(data=device_test_data)
            assert not serializer.is_valid()
            assert serializer.errors
            patched.assert_called_with(device_test_data[field_name])
            assert not set([field_name]) - set(serializer.errors.keys())


@pytest.mark.parametrize(
    ('field', 'value'),
    [('battery_per', bad) for bad in PERCENTAGE_VALUES_BAD]
    + [('cpu', bad) for bad in PERCENTAGE_VALUES_BAD]
    + [('resolution_y', bad) for bad in RESOLUTION_VALUES_BAD]
    + [('resolution_x', bad) for bad in RESOLUTION_VALUES_BAD]
    + [('pixel_density', bad) for bad in (None, '', 0, -1, 1024*10+1,
                                          'some_string')]
    + [('os', bad) for bad in (None, '', '\t', '\niOS', 'Ios', ' ios',
                               ' ios  ', 'a'*9, 'Android', 'android ')]
    + [('hardware_make', bad) for bad in (None, '', 'y', 'z'*65, 'Apple   ',
                                          ' Apple', ' Samsung ')]
    + [('hardware_model', bad) for bad in (None, '', 'y', 't'*65,
                                           '\niPhone 5 ', ' iPhone 5',
                                           '\tiPhone 5', 'a')]
    + [('os_version', bad) for bad in (None, '', 'g', '   8.0.2', '8.0.2\n',
                                       'r'*33)]
    + [('orientation', bad) for bad in (None, '', '\nportrait', 'portrait\r',
                                        'portrait   ', 'Landscape')]
    + [('orientation_deg', bad) for bad in (None, '', -1, 91, 'some_string')])
def test_device_fields_with_bad_data(field, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """Test a given field with a bad value.

    Makes sure that validation fails, and that reason is provided in
    serializer.errors.
    """
    device_test_data = get_device_test_data()
    device_test_data[field] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert not serializer.is_valid()
    assert not set([field]) - set(serializer.errors.keys())


@pytest.mark.parametrize(
    ('field', 'value'),
    [('resolution_y', bad) for bad in RESOLUTION_VALUES_GOOD]
    + [('resolution_x', bad) for bad in RESOLUTION_VALUES_GOOD]
    + [('battery_per', bad) for bad in PERCENTAGE_VALUES_GOOD]
    + [('cpu', bad) for bad in PERCENTAGE_VALUES_GOOD]
    + [('pixel_density', bad) for bad in (1, 1024*10)]
    + [('hardware_make', bad) for bad in ('HTC', 'Samsung', 'Apple', 'AB',
                                          'a'*64)]
    + [('hardware_model', bad) for bad in ('iPhone 5', 'iPhone 6plus',
                                           'Galaxy S', 'Galaxy S II',
                                           'Galaxy S5', 'GT-I9300', 'gH',
                                           'r'*64)]
    + [('os_version', bad) for bad in ('8.0.2', '7.1.1', '7.1', '2.3.7',
                                       '4.4.4', '1.1', 'b'*32)]
    + [('orientation', bad) for bad in ('landscape', 'portrait')]
    + [('orientation_deg', bad) for bad in (0, 90, 180, 270)]
    + [('user_agent', bad) for bad in
       ('Apple-iPhone2C1/901.334',
        'Apple-iPhone5C2/1001.525',
        'Apple-iPod5C1/1001.523',
        'Apple-iPad2C3/1001.403',
        'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',  # noqa
        'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',  # noqa
        'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',  # noqa
        'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',  # noqa
        'a'*2048)])
def test_device_fields_with_good_data(field, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """Test given field with good data."""
    device_test_data = get_device_test_data()
    device_test_data[field] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == getattr(serializer.object, field)


@pytest.mark.parametrize('value', ['ios', 'android'])
def test_validate_os_with_good_values(value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """Test os field."""
    device_test_data = get_device_test_data()
    device_test_data['os'] = value
    serializer = DeviceSerializer(data=device_test_data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors
    assert value == serializer.object.os_


DEVICE_GOOD_JSON = u"""
{
    "adid": "558D52FD-8B0A-4850-ADF4-FBC522D29F39",
    "battery_per": 57.6789,
    "cpu": 93.19216,
    "pixel_density": 157,
    "hardware_make": "Apple",
    "hardware_model": "iPhone 4s",
    "locale": "en_us",
    "orientation": "portrait",
    "orientation_deg": 0,
    "os": "ios",
    "os_version": "7.1.2",
    "resolution_x": 768,
    "resolution_y": 1024,
    "time": "2014-10-13T15:09:10Z",
    "tz": "UTC-08:00",
    "user_agent": "Apple-iPhone5C2/1001.525"
}
"""
