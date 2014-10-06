from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from selfieclub.serializers import UserSerializer


class EventView(APIView):
    # pylint: disable=too-many-public-methods
    def post(self, request, format=None):  # pylint: disable=redefined-builtin
        # noqa pylint: disable=unexpected-keyword-arg, no-value-for-parameter, no-member
        request_serializer = UserSerializer(data=request.DATA)
        if not request_serializer.is_valid():
            return Response(request_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        rest_response = Response(None, status=status.HTTP_200_OK)
        return rest_response
