"""This module contains the REST endpoints/views for Selfieclub."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from selfieclub.serializers import MemberSerializer


class EventView(APIView):

    """Event view."""

    # pylint: disable=too-many-public-methods
    def post(self, request, format=None):  # pylint: disable=redefined-builtin
        """Process incoming event that has been POSTed."""
        # noqa pylint: disable=unexpected-keyword-arg, no-value-for-parameter, no-member
        request_serializer = MemberSerializer(data=request.DATA)
        if not request_serializer.is_valid():
            return Response(request_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        rest_response = Response(None, status=status.HTTP_200_OK)
        return rest_response