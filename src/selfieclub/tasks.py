"""Analytics event processor."""

from __future__ import absolute_import
from celery.utils.log import get_task_logger
from celery import shared_task


LOGGER = get_task_logger(__name__)


@shared_task
def record_event(event):
    """Foo the bar."""
    LOGGER.debug('This is from the celery task \'debug\'...')
    LOGGER.info('This is from the celery task \'info\'...')
    LOGGER.warning('This is from the celery task \'warning\'...')
    LOGGER.error('This is from the celery task \'error\'...')
    LOGGER.critical('This is from the celery task \'critical\'...')
    LOGGER.info('Event to record: %s', event)


@shared_task
def echo(message):
    """Foo the bar."""
    LOGGER.error('Echo: %s', message)
    return message
