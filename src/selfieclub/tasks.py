"""Analytics event processor."""

from __future__ import absolute_import
from celery.utils.log import get_task_logger
from celery import shared_task
from selfieclub.serializers import AnalyticsEventSerializer


LOGGER = get_task_logger(__name__)


# @shared_task(bind=True, ignore_result=True, max_retries=5, )  # TODO - add
# self
@shared_task(ignore_result=True, max_retries=6,
             default_retry_delay=60*5)  # 6 reties, 5 min appart.
def record_event(event):
    # pylint: disable=no-member, no-value-for-parameter, unexpected-keyword-arg
    """Foo the bar."""
    serializer = AnalyticsEventSerializer(data=event)
    if not serializer.is_valid():
        LOGGER.warning('Invalid event.')
        LOGGER.debug('Invalid event details: %s', event)

    LOGGER.info('Event to record: %s', event)


@shared_task
def echo(message):
    """Foo the bar."""
    LOGGER.error('Echo: %s', message)
    return message
