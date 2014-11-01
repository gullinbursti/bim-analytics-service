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
        # pylint: disable=unexpected-keyword-arg, no-value-for-parameter
        # pylint: disable=no-member
        """Process incoming event that has been POSTed."""
        serializer = AnalyticsEventSerializer(data=request.DATA)
        if not serializer.is_valid():
            LOGGER.warning('Invalid message.')
            LOGGER.debug('Invalid message details: %s', request.DATA)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        # TODO - Message GUID
        LOGGER.info('Sending: TODO-GUID')
        LOGGER.debug('Sending message body: %s', serializer.data)
        tasks.record_event.delay(serializer.data)
        return Response(None, status=status.HTTP_200_OK)
