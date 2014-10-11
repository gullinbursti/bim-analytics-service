"""Unit tests for the Selfieclub event endpoint serializers."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
from io import StringIO
from mock import patch
from rest_framework.parsers import JSONParser
from selfieclub.serializers import UserSerializer
import pytest


@pytest.fixture(scope='module')
def user_test_data():
    # pylint: disable=function-redefined, global-variable-undefined
    # pylint: disable=invalid-name, unnecessary-lambda, redefined-outer-name
    """Return a copy of Member test data.

    This function uses closures, and redefines itself for efficency.  I am
    also doing a bit of experimentation.
    """
    stream = StringIO(USER_GOOD_JSON)
    data = JSONParser().parse(stream)
    global user_test_data
    user_test_data = lambda: data.copy()
    return data


@pytest.mark.usefixtures("django_setup")
class TestUserDeserialization(object):
    # pylint: disable=no-self-use, no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg, redefined-outer-name

    """Testing the Deserialization with UserSerializer."""

    @pytest.mark.parametrize(
        ('field_name', 'validator'),
        [('id', 'selfieclub.serializers.validate_user_id')])
    def test_calls_validator(self, user_test_data, field_name, validator):
        """Make sure that the proper validator has been called.

        Also makes certain that the the ValidationError() exception is being
        listened to.
        """
        with patch(validator) as patched:
            patched.side_effect = ValidationError('bee', 'boo')
            serializer = UserSerializer(data=user_test_data)
            assert not serializer.is_valid()
            assert serializer.errors
            assert not set([field_name]) - set(serializer.errors.keys())
            patched.assert_called_with(user_test_data[field_name])

    def test_loading_good_json_data_is_valid(self, user_test_data):
        """Test that loading good data works."""
        serializer = UserSerializer(data=user_test_data)
        assert serializer.is_valid()
        assert not serializer.errors
        user_dto = serializer.object
        assert user_test_data['cohort_date'] == user_dto.cohort_date
        assert user_test_data['cohort_week'] == user_dto.cohort_week
        assert user_test_data['name'] == user_dto.name
        assert user_test_data['id'] == user_dto.id_


USER_GOOD_JSON = u"""
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "user_name",
   "id" : 92837492
}
"""
