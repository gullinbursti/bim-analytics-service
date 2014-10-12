"""Unit tests for the Selfieclub event endpoint serializers."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
from io import StringIO
from mock import patch
from rest_framework.parsers import JSONParser
from selfieclub.serializers import MemberSerializer, DeviceSerializer
import pytest


@pytest.fixture(scope='module')
def member_test_data():
    # pylint: disable=function-redefined, global-variable-undefined
    # pylint: disable=invalid-name, unnecessary-lambda, redefined-outer-name
    """Return a copy of Member test data.

    This function uses closures, and redefines itself for efficency.  I am
    also doing a bit of experimentation.
    """
    stream = StringIO(MEMBER_GOOD_JSON)
    data = JSONParser().parse(stream)
    global member_test_data
    member_test_data = lambda: data.copy()
    return data


@pytest.fixture(scope='module')
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
class TestMemberDeserialization(object):
    # pylint: disable=no-self-use, no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg, redefined-outer-name

    """Testing the Deserialization with MemberSerializer."""

    @pytest.mark.parametrize(
        ('field_name', 'validator'),
        [('id', 'selfieclub.serializers.validate_member_id'),
         ('name', 'selfieclub.serializers.validate_member_name'),
         ('cohort_date', 'selfieclub.serializers.validate_cohort_date'),
         ('cohort_week', 'selfieclub.serializers.validate_cohort_week')])
    def test_calls_validator(self, member_test_data, field_name, validator):
        """Make sure that the proper validator has been called.

        Also makes certain that the the ValidationError() exception is being
        listened to.
        """
        with patch(validator) as patched:
            patched.side_effect = ValidationError(
                'Fake validation error in unit testing.', 'boo')
            serializer = MemberSerializer(data=member_test_data)
            assert not serializer.is_valid()
            assert serializer.errors
            patched.assert_called_with(member_test_data[field_name])
            assert not set([field_name]) - set(serializer.errors.keys())

    def test_loading_good_json_data_is_valid(self, member_test_data):
        """Test that loading good data works."""
        serializer = MemberSerializer(data=member_test_data)
        assert serializer.is_valid()
        assert not serializer.errors
        member_dto = serializer.object
        assert member_test_data['cohort_date'] == member_dto.cohort_date
        assert member_test_data['cohort_week'] == member_dto.cohort_week
        assert member_test_data['name'] == member_dto.name
        assert member_test_data['id'] == member_dto.id_


@pytest.mark.usefixtures("django_setup")
class TestDeviceDeserialization(object):
    # pylint: disable=no-self-use, no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg, redefined-outer-name
    # pylint: disable=too-few-public-methods

    """Testing the Deserialization with MemberSerializer."""

    @pytest.mark.parametrize(
        ('field_name', 'validator'),
        [('adid', 'selfieclub.serializers.validate_device_adid'),
         ('battery_per', 'selfieclub.serializers.validate_device_battery_per'),
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
         ('resolution', 'selfieclub.serializers.validate_device_resolution'),
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

DEVICE_GOOD_JSON = u"""
{
    "adid": "TODO - fix adid",
    "battery_per": "TODO - fix battery_per",
    "cpu": "TODO - fix cpu",
    "density": "TODO - fix density",
    "hardware_make": "TODO - fix hardware_make",
    "hardware_model": "TODO - fix hardware_model",
    "locale": "TODO - fix locale",
    "orientation": "TODO - fix orientation",
    "orientation_deg": "TODO - fix orientation_deg",
    "os": "TODO - fix os",
    "os_version": "TODO - fix os_version",
    "resolution": "TODO - fix resolution",
    "time": "TODO - fix time",
    "token": "TODO - fix token",
    "tz": "TODO - fix tz",
    "user_agent": "TODO - fix user_agent"
}
"""

MEMBER_GOOD_JSON = u"""
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "member_name",
   "id" : 92837492
}
"""
