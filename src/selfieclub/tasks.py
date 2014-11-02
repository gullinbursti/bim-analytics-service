"""Analytics event processor."""

from __future__ import absolute_import
from celery.utils.log import get_task_logger
from celery import shared_task
from django.conf import settings
from selfieclub.serializers import AnalyticsEventSerializer
from keen.exceptions import KeenApiError
import keen


LOGGER = get_task_logger(__name__)


@shared_task(bind=True, ignore_result=True, max_retries=6,
             default_retry_delay=60*5)  # 6 reties, 5 min appart.
def record_event(self, event):
    # pylint: disable=no-member, no-value-for-parameter, unexpected-keyword-arg
    """Send client analitics event to Keen IO."""
    serializer = AnalyticsEventSerializer(data=event)
    if not serializer.is_valid():
        # Note that if serialization fails, serializer.data is bad, use
        # original event.
        LOGGER.warning('Invalid event: %s', serializer.errors)
        LOGGER.debug('Invalid event details: %s', event)
        return

    try:
        # TODO - Record event GUID
        LOGGER.info('Event to record (attempt# %s): TODO-GUID',
                    self.request.retries)
        LOGGER.debug('Event to record details: %s', serializer.data)
        keen.add_event(settings.KEEN_IO_EVENT_COLLECTIONS['client_event'],
                       serializer.data)
    except KeenApiError as exception:
        LOGGER.exception('Failed to record event to upstream.',
                         exc_info=exception)
        raise self.retry(exc=exception)
