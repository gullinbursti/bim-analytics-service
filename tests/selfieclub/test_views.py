"""Unit tests for the Selfieclub event endpoint views."""

from __future__ import absolute_import
from mock import patch
from rest_framework import status
from rest_framework.test import APIRequestFactory
from selfieclub.views import EventView


class TestEventView(object):
    # pylint: disable=no-self-use, unused-argument, too-few-public-methods

    """Testing the EventView."""

    @patch('selfieclub.views.AnalyticsEventSerializer')
    def test_posting_a_good_event(self, mock_serializer):
        """Just check to make sure that the serializer is being used.

        The idea is that the serializer is being tested somewhere else.  As
        long as the view uses the serializer correctly, and returns the result
        we are OK.
        """
        # ** Arrange **
        mock_instance = mock_serializer.return_value
        mock_instance.is_valid.return_value = True
        factory = APIRequestFactory()
        request = factory.post('/selfieclub/', {'title': 'new idea'})
        view = EventView.as_view()
        # ** Act **
        response = view(request)
        # ** Assert **
        mock_instance.is_valid.assert_called()
        assert status.HTTP_200_OK == response.status_code
        assert not response.data

    @patch('selfieclub.views.AnalyticsEventSerializer')
    def test_posting_a_bad_event(self, mock_serializer):
        """Just check to make sure that the serializer is being used.

        The idea is that the serializer is being tested somewhere else.  As
        long as the view uses the serializer correctly, and returns the result
        we are OK.
        """
        # ** Arrange **
        fake_error = {'cohort_week': [u'This field is required.']}
        mock_instance = mock_serializer.return_value
        mock_instance.is_valid.return_value = False
        mock_instance.errors = fake_error
        factory = APIRequestFactory()
        request = factory.post('/selfieclub/', {'title': 'new idea'})
        view = EventView.as_view()
        # ** Act **
        response = view(request)
        # ** Assert **
        mock_instance.is_valid.assert_called()
        assert status.HTTP_400_BAD_REQUEST == response.status_code
        assert fake_error == response.data
