"""Test BIM Analytics selfieclub tasks."""

from __future__ import absolute_import
from keen.exceptions import KeenApiError
from mock import patch
from selfieclub import tasks
import selfieclub


@patch('selfieclub.tasks.settings.CELERY_ALWAYS_EAGER', True, create=True)
def test_record_event_successful_send():
    """Test that event is send to Keen when all i s good."""
    with patch('selfieclub.tasks.AnalyticsEventSerializer') as clazz, \
            patch('selfieclub.tasks.keen') as keen:
        # Arrange
        serializer = clazz.return_value
        serializer.is_valid.return_value = True
        # Act
        # TODO - Pass in an actual dict
        tasks.record_event.delay({'faking': 'it'})
        # Assert
        serializer.is_valid.assert_called()
        keen.add_event.assert_called_with('Basic Client Event - DEVINT',
                                          serializer.data)


@patch('selfieclub.tasks.settings.CELERY_ALWAYS_EAGER', True, create=True)
def test_record_event_invalid_data_does_not_send():
    """Test that invalid data is dropped, and not sent to Keen."""
    with patch('selfieclub.tasks.AnalyticsEventSerializer') as clazz, \
            patch('selfieclub.tasks.keen') as keen:
        # Arrange
        serializer = clazz.return_value
        serializer.is_valid.return_value = False
        # Act
        # TODO - Pass in an actual dict
        tasks.record_event.delay({'faking': 'it'})
        # Assert
        serializer.is_valid.assert_called()
        assert not keen.add_event.mock_calls


@patch('selfieclub.tasks.settings.CELERY_ALWAYS_EAGER', True, create=True)
def test_record_event_rety_on_keen_error():
    """Test that an even is requeued for retying on Keen exceptions."""
    with patch('selfieclub.tasks.AnalyticsEventSerializer') as clazz, \
            patch('selfieclub.tasks.keen') as keen, \
            patch.object(selfieclub.tasks.record_event, 'retry') as retry:
        # Arrange
        serializer = clazz.return_value
        serializer.is_valid.return_value = True
        exception = KeenApiError({
            'message': 'mock message',
            'error_code': 500})
        keen.add_event.side_effect = exception
        retry.return_value = exception
        # Act
        # TODO - Pass in an actual dict
        tasks.record_event.delay({'faking': 'it'})
        # Assert
        keen.add_event.assert_called()
        retry.assert_called()
        # retry.assert_called_with(exc=exception)
