"""Selfieclub event serializers."""

from __future__ import absolute_import
from . import dtos
from bimcore.validators.member import validate_cohort_date
from bimcore.validators.member import validate_cohort_week
from bimcore.validators.member import validate_member_name
from bimcore.validators.member import validate_member_id
from rest_framework import serializers


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

    def validate_name(self, attrs, source):
        """member name validation call."""
        validate_member_name(attrs[source])
        return attrs

    def validate_cohort_week(self, attrs, source):
        """member cohort week validation call."""
        validate_cohort_week(attrs[source])
        return attrs

    def validate_cohort_date(self, attrs, source):
        """member cohort date validation call."""
        validate_cohort_date(attrs[source])
        return attrs
