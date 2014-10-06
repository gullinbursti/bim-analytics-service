from rest_framework.test import APIRequestFactory
from selfieclub.views import EventView


class TestEventView(object):
    # pylint: disable=no-self-use, unused-argument, too-few-public-methods
    def test_posting_a_good_event(self, django_setup):
        factory = APIRequestFactory()
        request = factory.post('/selfieclub/', {'title': 'new idea'})
        view = EventView.as_view()
        response = view(request)
        assert response
