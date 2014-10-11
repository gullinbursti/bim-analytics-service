"""Selfieclub event serializers."""

from __future__ import absolute_import
from . import dtos
from rest_framework import serializers
from bimcore.validators.member import validate_member_id


class MemberSerializer(serializers.Serializer):
    # pylint: disable=no-self-use

    """member information serializer."""

    # member ID
    id = serializers.IntegerField(  # pylint: disable=invalid-name
        required=True,
        )
    # member name
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
        """Given a dictionary of deserialized field values."""
        assert instance is None, 'Cannot be used to update, only to create'
        return dtos.MemberDto(
            attrs['id'],
            attrs['name'],
            attrs['cohort_date'],
            attrs['cohort_week'])

    def validate_id(self, attrs, source):
        """member ID validation call."""
        validate_member_id(attrs[source])
        return attrs
