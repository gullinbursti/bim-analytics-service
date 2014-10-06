"""Unit tests for the Selfieclub event endpoint views."""

from rest_framework.test import APIRequestFactory
from selfieclub.views import EventView


class TestEventView(object):
    # pylint: disable=no-self-use, unused-argument, too-few-public-methods

    """Testing the EventView."""

    def test_posting_a_good_event(self, django_setup):
        """Make sure POSTING a good event works."""
        factory = APIRequestFactory()
        request = factory.post('/selfieclub/', {'title': 'new idea'})
        view = EventView.as_view()
        response = view(request)
        assert response
