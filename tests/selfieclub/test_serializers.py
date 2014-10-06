"""Unit tests for the Selfieclub event endpoint serializers."""

from __future__ import absolute_import
from io import StringIO
from rest_framework.parsers import JSONParser
from selfieclub.serializers import UserSerializer


class FieldTestValues(object):

    """Helper class to maintain good, and bad values for a given field."""

    _good_values = (None,)
    _bad_values = (None,)

    @property
    def good_values(self):
        """Read-only tuple of good values."""
        return self._good_values

    @property
    def bad_values(self):
        """Read-only tuple of bad values."""
        return self._bad_values

    @property
    def good_value(self):
        """A known good value."""
        return self._good_values[0]

    @property
    def bad_value(self):
        """A known bad value."""
        return self._bad_values[0]


class UserIdTestValues(FieldTestValues):

    """Contains test values for user IDs."""

    _good_values = (
        92837492,)
    _bad_values = (
        None,
        -1,)


class UserNameTestValues(FieldTestValues):

    """Contains test values for user names."""

    _good_values = (
        'jerry',)
    _bad_values = (
        None,
        '',)


class DataGenerator(object):

    """Data generator, for use with FieldTestValues' children."""

    def __init__(self, data):
        """Create an instance of DataGenerator."""
        self.data = data

    def good_variation(self):
        """Return a dictionary with good vaules in all the fields."""
        good = {}
        for key in self.data.keys():
            good[key] = self.data[key].good_value
        return good

    def bad_variations(self):
        """Return an array with bad data combinations for testing."""
        good_base_line = self.good_variation()
        variations = []
        for key in self.data.keys():
            for bad_value in self.data[key].bad_values:
                bad_copy = good_base_line.copy()
                bad_copy[key] = bad_value
                variations.append({
                    'data': bad_copy,
                    'expected_bad': [key]})
        return variations


class TestUserDeserialization(object):
    # pylint: disable=too-few-public-methods, no-self-use
    # pylint: disable=no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg

    """Testing the Deserialization with UserSerializer."""

    def test_loading_good_json_data_is_valid(self):
        """Test that loading good data works."""
        stream = StringIO(USER_GOOD_JSON)
        data_dict = JSONParser().parse(stream)
        serializer = UserSerializer(data=data_dict)
        assert serializer.is_valid()
        assert not serializer.errors
        user_dto = serializer.object
        assert data_dict['cohort_date'] == user_dto.cohort_date
        assert data_dict['cohort_week'] == user_dto.cohort_week
        assert data_dict['name'] == user_dto.name
        assert data_dict['id'] == user_dto.id_


USER_GOOD_JSON = u"""
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "user_name",
   "id" : 92837492
}
"""
