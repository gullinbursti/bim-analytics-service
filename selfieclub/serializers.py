"""Selfieclub event serializers."""

from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    # pylint: disable=too-few-public-methods

    """User information serializer."""

    # User ID
    id = serializers.CharField(  # pylint: disable=invalid-name
        required=True,
        )
    # User name
    name = serializers.CharField(
        required=True,
        )
    # In the work of 'YYYY-WW', where WW is week number.
    cohort_week = serializers.CharField(
        required=True,
        )
    # In the form of 'YYYY-MM-DD'.
    cohort_date = serializers.CharField(
        required=True,
        )
