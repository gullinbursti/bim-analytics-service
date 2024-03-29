"""Unit tests for the Selfieclub event endpoint serializers."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
from io import StringIO
from mock import patch
from rest_framework.parsers import JSONParser
from selfieclub.serializers import MemberSerializer, \
    AnalyticsEventSerializer, StateInfoSerializer, ApplicationSerializer, \
    SessionSerializer
from tests.selfieclub.test_serializers_device import get_device_test_data
from bimtest.values import GuidTestValues
import pytest
import sys


# -----------------------------------------------------------------------------
# MemberSerializer
# -----------------------------------------------------------------------------
MEMBER_GOOD_JSON = u"""
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "member_name",
   "identifier" : 92837492
}
"""


def get_member_test_data():
    """Return a copy of Member test data."""
    stream = StringIO(MEMBER_GOOD_JSON)
    return JSONParser().parse(stream)


class TestMemberDeserialization(object):
    # pylint: disable=no-self-use, no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg, redefined-outer-name

    """Testing the Deserialization with MemberSerializer."""

    @pytest.mark.parametrize(
        ('field_name', 'validator'),
        [('identifier', 'selfieclub.serializers.validate_member_id'),
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

    # TODO: Test various known good values
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
        assert member_test_data['identifier'] == member_dto.identifier


# -----------------------------------------------------------------------------
# StateInfoSerializer
# -----------------------------------------------------------------------------
STATE_INFO_GOOD_JSON = u"""
{
    "screen_current": "CLUB_EVENTS_VIEW_01",
    "screen_previous": "HOME_SCREEN",
    "action_current": "SEARCH",
    "action_previous": "OPEN"
}
"""

STATE_INFO_BAD_STATE = (
    None,
    '',
    'X' * 3,
    'Y' * 33,
    'ZZZZZZZZ ',
    ' ZZZZZZZZ ',
    '\tZZZZZZZZ',
    'ZZZZZZZZ\n',
    '\nZZZZZZZZ'
)


def get_state_info_test_data():
    """Return a copy of Member test data."""
    stream = StringIO(STATE_INFO_GOOD_JSON)
    return JSONParser().parse(stream)


@pytest.mark.parametrize(
    ('field', 'value'),
    [('screen_current', bad) for bad in STATE_INFO_BAD_STATE]
    + [('screen_previous', bad) for bad in STATE_INFO_BAD_STATE]
    + [('action_current', bad) for bad in STATE_INFO_BAD_STATE]
    + [('action_previous', bad) for bad in STATE_INFO_BAD_STATE])
def test_state_info_fields_with_bad_data(field, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """Test a given field with a bad value.

    Makes sure that validation fails, and that reason is provided in
    serializer.errors.
    """
    data = get_state_info_test_data()
    data[field] = value
    serializer = StateInfoSerializer(data=data)
    assert not serializer.is_valid(), serializer.errors
    assert not set([field]) - set(serializer.errors.keys())


# TODO: Test DTO, and various known good values
def test_state_info_fields_with_good_data():
    # pylint: disable=unexpected-keyword-arg, no-value-for-parameter
    # pylint: disable=no-member
    """Test StateInfoSerializer with good data, our base line.."""
    data = get_state_info_test_data()
    serializer = StateInfoSerializer(data=data)
    assert serializer.is_valid(), serializer.errors


# -----------------------------------------------------------------------------
# ApplicationSerializer
# -----------------------------------------------------------------------------
APPLICATION_GOOD_JSON = u"""
{
    "client_version": "1.27.3",
    "service_env": "prod",
    "service_volley_version": "sc0007",
    "service_selfieclub_version": "2.79.93",
    "service_bimanalytics_version": "0.13.4"
}
"""

APPLICATION_BAD_STATE = (
    None,
    '',
    'X' * 3,
    'Y' * 33,
    'ZZZZZZZZ ',
    ' ZZZZZZZZ ',
    '\tZZZZZZZZ',
    'ZZZZZZZZ\n',
    '\nZZZZZZZZ'
)


def get_application_test_data():
    """Return a copy of Member test data."""
    stream = StringIO(APPLICATION_GOOD_JSON)
    return JSONParser().parse(stream)


@pytest.mark.parametrize(
    ('field', 'value'),
    [('client_version', bad) for bad in APPLICATION_BAD_STATE]
    + [('service_env', bad) for bad in APPLICATION_BAD_STATE]
    + [('service_volley_version', bad) for bad in APPLICATION_BAD_STATE]
    + [('service_selfieclub_version', bad) for bad in APPLICATION_BAD_STATE]
    + [('service_bimanalytics_version', bad) for bad in APPLICATION_BAD_STATE])
def test_application_fields_with_bad_data(field, value):
    # pylint: disable=redefined-outer-name, unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter, no-member
    """Test a given field with a bad value.

    Makes sure that validation fails, and that reason is provided in
    serializer.errors.
    """
    data = get_application_test_data()
    data[field] = value
    serializer = ApplicationSerializer(data=data)
    assert not serializer.is_valid(), serializer.errors
    assert not set([field]) - set(serializer.errors.keys())


# TODO: Test DTO, and various known good values
def test_application_fields_with_good_data():
    # pylint: disable=unexpected-keyword-arg, no-value-for-parameter
    # pylint: disable=no-member
    """Test ApplicationSerializer with good data, our base line.."""
    data = get_application_test_data()
    serializer = ApplicationSerializer(data=data)
    assert serializer.is_valid(), serializer.errors


# -----------------------------------------------------------------------------
# SessionSerializer
# -----------------------------------------------------------------------------
SESSION_GOOD_JSON = u"""
{
    "identifier": "7068C396-1D49-4AEE-9304-6D4410E56E39",
    "identifier_last": "7D61B5ED-E750-4D5F-9D06-8FC787121128",
    "event_identifier": "92FBC6F2-AD5F-4FD1-B838-0D8DBABB6263",
    "session_gap": 852877,
    "duration": 10789,
    "idle": 398,
    "count": 23,
    "entry_point": "push_notification"
}
"""

_BAD_POSITIVE_INTEGERS = ('', None, ' ', False, True, -1)
_GOOD_POSITIVE_INTEGERS = (0, sys.maxsize)


def get_session_test_data():
    """Return a copy of Member test data."""
    stream = StringIO(SESSION_GOOD_JSON)
    return JSONParser().parse(stream)


def test_session_serializer_with_good_data():
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Test SessionSerializer with good data."""
    serializer = SessionSerializer(data=get_session_test_data())
    assert serializer.is_valid(), serializer.errors


@pytest.mark.parametrize(
    ('field', 'value'),
    [('identifier', bad_value) for bad_value in GuidTestValues().bad_values]
    + [('identifier_last', bad_value)
       for bad_value in GuidTestValues().bad_values]
    + [('event_identifier', bad_value)
       for bad_value in GuidTestValues().bad_values]
    + [('session_gap', bad_value) for bad_value in _BAD_POSITIVE_INTEGERS]
    + [('duration', bad_value) for bad_value in _BAD_POSITIVE_INTEGERS]
    + [('idle', bad_value) for bad_value in _BAD_POSITIVE_INTEGERS]
    + [('count', bad_value) for bad_value in _BAD_POSITIVE_INTEGERS]
    + [('entry_point', bad_value)
       for bad_value in ['home ', '\nhome', 'home\n', 'home\t', 'hOme'
                         '', ' ', None]])
def test_session_serializer_with_bad_values(field, value):
    # pylint: disable=no-value-for-parameter, unexpected-keyword-arg, no-member
    """Test with a variety of bad values."""
    data = get_session_test_data()
    data[field] = value
    serializer = SessionSerializer(data=data)
    assert not serializer.is_valid()
    assert not set([field]) - set(serializer.errors.keys())


@pytest.mark.parametrize(
    ('field', 'value'),
    [('identifier', good_value) for good_value in GuidTestValues().good_values]
    + [('identifier_last', good_value)
       for good_value in GuidTestValues().good_values]
    + [('event_identifier', good_value)
       for good_value in GuidTestValues().good_values]
    + [('session_gap', good_value) for good_value in _GOOD_POSITIVE_INTEGERS]
    + [('duration', good_value) for good_value in _GOOD_POSITIVE_INTEGERS]
    + [('idle', good_value) for good_value in _GOOD_POSITIVE_INTEGERS]
    + [('count', good_value) for good_value in _GOOD_POSITIVE_INTEGERS]
    + [('entry_point', good_value)
       for good_value in ['home', 'push_notification']])
def test_session_serializer_with_good_values(field, value):
    # pylint: disable=no-value-for-parameter, unexpected-keyword-arg, no-member
    """Test with a variety or good values."""
    data = get_session_test_data()
    data[field] = value
    serializer = SessionSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    assert not serializer.errors.keys()


@pytest.mark.parametrize('field', get_session_test_data().keys())
def test_session_serializer_with_missing_fields(field):
    # pylint: disable=no-value-for-parameter, unexpected-keyword-arg, no-member
    """Test with missing fields."""
    data = get_session_test_data()
    del data[field]
    serializer = SessionSerializer(data=data)
    assert not serializer.is_valid()
    assert not set([field]) - set(serializer.errors.keys())


# -----------------------------------------------------------------------------
# AnalyticsEventSerializer
# -----------------------------------------------------------------------------
_ANALYTICSEVENT_KEY_COMBINATIONS = (
    ('member',),
    ('device',),
    ('state_info',),
    ('application',),
    ('session',),
    ('session', 'member',),
    ('session', 'device',),
    ('session', 'state_info',),
    ('session', 'application',),
    ('session', 'member', 'state_info'),
    ('session', 'member', 'device'),
    ('session', 'device', 'state_info'),
    ('session', 'member', 'device', 'state_info'),
    ('session', 'application', 'member',),
    ('session', 'application', 'device',),
    ('session', 'application', 'state_info',),
    ('session', 'application', 'member', 'state_info'),
    ('session', 'application', 'member', 'device'),
    ('session', 'application', 'device', 'state_info'),
    ('session', 'application', 'member', 'device', 'state_info'))


def get_analytics_event_data():
    """Provide a analytics event test data."""
    return {'member': get_member_test_data(),
            'application': get_application_test_data(),
            'device': get_device_test_data(),
            'state_info': get_state_info_test_data(),
            'session': get_session_test_data()}


@pytest.mark.parametrize(
    'missing', _ANALYTICSEVENT_KEY_COMBINATIONS)
def test_analyticseventserializer_has_missing_values(missing):
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Confirm not vaild on missing required fields.

    Making sure that missing required fields mark the serializer object as
    invalid, and that they are listed in serializer.errors.
    """
    data = get_analytics_event_data()
    for key in missing:
        del data[key]
    serializer = AnalyticsEventSerializer(data=data)
    assert not serializer.is_valid()
    for there in data.keys():
        assert there not in serializer.errors.keys()


@pytest.mark.parametrize(
    'nones', _ANALYTICSEVENT_KEY_COMBINATIONS)
def test_analyticseventserializer_has_none_values(nones):
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Confirm not vaild on required fields set to None.

    In this case we are making sure that required fields with `None` values
    results in an invalid state.  We also make sure that the the
    serializer.errors property contains a list of the None valued keys.
    """
    data = get_analytics_event_data()
    for key in nones:
        data[key] = None
    serializer = AnalyticsEventSerializer(data=data)
    assert not serializer.is_valid()
    # excpected bad keys == actual bad keys
    assert set(nones) == set(serializer.errors.keys()), serializer.errors


@pytest.mark.parametrize(
    'empties', _ANALYTICSEVENT_KEY_COMBINATIONS)
def test_analyticseventserializer_has_bad_values(empties):
    # pylint: disable=no-value-for-parameter, no-member, unexpected-keyword-arg
    """Confirm that nested serializers are validated.

    Cheating a bit by feeding in empty data (empty dict {}) into into the
    fields being tested.  We confirm that serializer.errors flags the
    appropriate bad flieds, as well as that the individual nested serialization
    errors are sending back more than one error.
    """
    data = get_analytics_event_data()
    for key in empties:
        data[key] = {}
    serializer = AnalyticsEventSerializer(data=data)
    assert not serializer.is_valid()
    assert set(empties) == set(serializer.errors.keys())
    for key in empties:
        assert len(serializer.errors[key][0].keys()) > 1
