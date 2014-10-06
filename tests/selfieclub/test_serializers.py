import json
from selfieclub.serializers import UserSerializer


class TestUserSerializer(object):
    # pylint: disable=too-few-public-methods, no-self-use
    # pylint: disable=no-value-for-parameter, no-member
    # pylint: disable=unexpected-keyword-arg
    def test_loading_good_json(self):
        data = json.loads(USER_GOOD_JSON)
        user = UserSerializer(data=data)
        assert user.is_valid()
        assert not user.errors


USER_GOOD_JSON = """
{
   "cohort_date" : "2014-10-05",
   "cohort_week" : "2014-32",
   "name" : "user_name",
   "id" : 92837492
}
"""
