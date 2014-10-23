"""Unit tests for the Selfieclub event endpoint serializers."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
from io import StringIO
from mock import patch
from rest_framework.parsers import JSONParser
from selfieclub.serializers import MemberSerializer, AnalyticsEventSerializer
import pytest
from tests.selfieclub.test_serializers_device import get_device_test_data

MEMBER_GOOD_JSON = u"""
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "member_name",
   "id" : 92837492
}
"""


def get_member_test_data():
    # pylint: disable=function-redefined, global-variable-undefined
    # pylint: disable=invalid-name, unnecessary-lambda, redefined-outer-name
    """Return a copy of Member test data.

    This function uses closures, and redefines itself for efficency.  I am
    also doing a bit of experimentation.
    """
    stream = StringIO(MEMBER_GOOD_JSON)
    data = JSONParser().parse(stream)
    global get_member_test_data
    get_member_test_data = lambda: data.copy()
    return data


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
    def test_calls_validator(self, field_name, validator):
        """Make sure that the proper validator has been called.

        Also makes certain that the the ValidationError() exception is being
        listened to.
        """
        member_test_data = get_member_test_data()
        with patch(validator) as patched:
            patched.side_effect = ValidationError(
                'Fake validation error in unit testing.', 'boo')
            serializer = MemberSerializer(data=member_test_data)
            assert not serializer.is_valid()
            assert serializer.errors
            patched.assert_called_with(member_test_data[field_name])
            assert not set([field_name]) - set(serializer.errors.keys())

    def test_loading_good_json_data_is_valid(self):
        """Test that loading good data works."""
        member_test_data = get_member_test_data()
        serializer = MemberSerializer(data=member_test_data)
        assert serializer.is_valid()
        assert not serializer.errors
        member_dto = serializer.object
        assert member_test_data['cohort_date'] == member_dto.cohort_date
        assert member_test_data['cohort_week'] == member_dto.cohort_week
        assert member_test_data['name'] == member_dto.name
        assert member_test_data['id'] == member_dto.id_


@pytest.mark.parametrize(
    'data', [
        {'member': get_member_test_data()},
        {'device': get_device_test_data()},
        {}])
def test_analyticseventserializer_has_missing_values(data):
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Confirm not vaild on missing required fields.

    Making sure that missing required fields mark the serializer object as
    invalid, and that they are listed in serializer.errors.
    """
    serializer = AnalyticsEventSerializer(data=data)
    assert not serializer.is_valid()
    for there in data.keys():
        assert there not in serializer.errors.keys()


@pytest.mark.parametrize(
    'data', [
        {'member': get_member_test_data(), 'device': None},
        {'member': None, 'device': get_device_test_data()},
        {'member': None, 'device': None}])
def test_analyticseventserializer_has_none_values(data):
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Confirm not vaild on required fields set to None.

    In this case we are making sure that required fields with `None` values
    results in an invalid state.  We also make sure that the the
    serializer.errors property contains a list of the None valued keys.
    """
    serializer = AnalyticsEventSerializer(data=data)
    assert not serializer.is_valid()
    # excpected bad keys == actual bad keys
    assert set([key for key, value in data.items() if value is None]) \
        == set(serializer.errors.keys())


@pytest.mark.parametrize(
    'data', [
        {'member': get_member_test_data(), 'device': {}},
        {'member': {}, 'device': get_device_test_data()},
        {'member': {}, 'device': {}}])
def test_analyticseventserializer_has_bad_values(data):
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Confirm that nested serializers are validated.

    Cheating a bit by feeding in empty data (empty dict {}) into into the
    fields being tested.  We confirm that serializer.errors flags the
    appropriate bad flieds, as well as that the individual nested serialization
    errors are sending back more than one error.
    """
    serializer = AnalyticsEventSerializer(data=data)
    expected = set([key for key, value in data.items() if not value])
    assert not serializer.is_valid()
    assert expected == set(serializer.errors.keys())
    for key in expected:
        assert len(serializer.errors[key][0].keys()) > 1
