"""This module contains the REST endpoints/views for Selfieclub."""

from __future__ import absolute_import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from selfieclub import tasks
from selfieclub.serializers import AnalyticsEventSerializer
import logging


LOGGER = logging.getLogger(__name__)


class EventView(APIView):

    """Event view."""

    # pylint: disable=too-many-public-methods
    def post(self, request, format=None):  # pylint: disable=redefined-builtin
        # noqa pylint: disable=unexpected-keyword-arg, no-value-for-parameter, no-member
        """Process incoming event that has been POSTed."""
        request_serializer = AnalyticsEventSerializer(data=request.DATA)
        if not request_serializer.is_valid():
            return Response(request_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        LOGGER.debug('This is from the django view \'debug\'...')
        LOGGER.info('This is from the django view \'info\'...')
        LOGGER.warning('This is from the django view \'warning\'...')
        LOGGER.error('This is from the django view \'error\'...')
        LOGGER.critical('This is from the django view \'critical\'...')
        LOGGER.info('Sending: %s', request_serializer)
        tasks.record_event.delay(request_serializer.data)

        rest_response = Response(None, status=status.HTTP_200_OK)
        return rest_response
