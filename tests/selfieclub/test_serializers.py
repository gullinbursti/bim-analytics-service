"""Unit tests for the Selfieclub event endpoint serializers."""

from __future__ import absolute_import
from StringIO import StringIO
from rest_framework.parsers import JSONParser
from selfieclub.serializers import UserSerializer


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


USER_GOOD_JSON = """
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "user_name",
   "id" : 92837492
}
"""
