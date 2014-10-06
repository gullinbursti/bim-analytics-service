"""Selfieclub event serializers."""

from __future__ import absolute_import
from . import dtos
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    # Mostly implemented in parent.  pylint: disable=too-few-public-methods

    """User information serializer."""

    # User ID
    id = serializers.IntegerField(  # pylint: disable=invalid-name
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

    def restore_object(self, attrs, instance=None):
        # Overriding `restore_object` from parent.  pylint: disable=no-self-use
        """Given a dictionary of deserialized field values."""
        assert instance is None, 'Cannot be used to update, only to create'
        return dtos.UserDto(
            attrs['id'],
            attrs['name'],
            attrs['cohort_date'],
            attrs['cohort_week'])
