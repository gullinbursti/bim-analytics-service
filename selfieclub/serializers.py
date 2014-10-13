"""Selfieclub event serializers."""

from __future__ import absolute_import
from . import dtos
from bimcore.validators import IntegerValidator, DecimalValidator
from bimcore.validators.analytics.device import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import
from bimcore.validators.member import validate_cohort_date
from bimcore.validators.member import validate_cohort_week
from bimcore.validators.member import validate_member_id
from bimcore.validators.member import validate_member_name
from bimcore.validators import validate_not_white_space_padded, \
    validate_not_none
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from rest_framework import serializers


class MemberSerializer(serializers.Serializer):
    # pylint: disable=no-self-use

    """Member information serializer."""

    id = serializers.IntegerField(required=True)  # noqa pylint: disable=invalid-name
    name = serializers.CharField(required=True)
    cohort_week = serializers.CharField(required=True)
    cohort_date = serializers.CharField(required=True)

    def restore_object(self, attrs, instance=None):
        """Given a dictionary of deserialized field values."""
        assert instance is None, 'Cannot be used to update, only to create'
        return dtos.MemberDto(
            id_=attrs['id'],
            name=attrs['name'],
            cohort_date=attrs['cohort_date'],
            cohort_week=attrs['cohort_week'])

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


class DeviceSerializer(serializers.Serializer):
    # pylint: disable=no-self-use

    """Device information validators."""

    adid = serializers.CharField(required=True)
    battery_per = serializers.DecimalField(required=True)
    cpu = serializers.DecimalField(required=True)
    pixel_density = serializers.IntegerField(required=True)
    hardware_make = serializers.CharField(required=True)
    hardware_model = serializers.CharField(required=True)
    locale = serializers.CharField(required=True)
    orientation = serializers.CharField(required=True)
    orientation_deg = serializers.CharField(required=True)
    os = serializers.CharField(required=True)  # pylint: disable=invalid-name
    os_version = serializers.CharField(required=True)
    resolution_x = serializers.IntegerField(required=True)
    resolution_y = serializers.IntegerField(required=True)
    time = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    tz = serializers.CharField(required=True)  # pylint: disable=invalid-name
    user_agent = serializers.CharField(required=True)

    def restore_object(self, attrs, instance=None):
        """Given a dictionary of deserialized field values."""
        assert instance is None, 'Cannot be used to update, only to create'
        return dtos.DeviceDto(
            adid=attrs['adid'],
            battery_per=attrs['battery_per'],
            cpu=attrs['cpu'],
            pixel_density=attrs['pixel_density'],
            hardware_make=attrs['hardware_make'],
            hardware_model=attrs['hardware_model'],
            locale=attrs['locale'],
            orientation=attrs['orientation'],
            orientation_deg=attrs['orientation_deg'],
            os_=attrs['os'],
            os_version=attrs['os_version'],
            resolution_x=attrs['resolution_x'],
            resolution_y=attrs['resolution_y'],
            time=attrs['time'],
            token=attrs['token'],
            tz_=attrs['tz'],
            user_agent=attrs['user_agent'])

    def validate_os(self, attrs, source):
        """Validate os."""
        if len(attrs[source]) > 8:
            raise ValidationError('String length greater than 8.')
        if attrs[source] not in ('ios', 'android'):
            raise ValidationError(
                'Valid value is either \'ios\' or \'android\'.')
        return attrs

    def validate_os_version(self, attrs, source):
        """Validate os_version."""
        validate_not_none(attrs[source])
        (MaxLengthValidator(32))(attrs[source])
        validate_not_white_space_padded(attrs[source])
        (MinLengthValidator(2))(attrs[source])
        return attrs

    def validate_hardware_make(self, attrs, source):
        """Validate hardware_make."""
        validate_not_none(attrs[source])
        (MaxLengthValidator(64))(attrs[source])
        validate_not_white_space_padded(attrs[source])
        (MinLengthValidator(2))(attrs[source])
        return attrs

    def validate_hardware_model(self, attrs, source):
        """Validate hardware_model."""
        validate_not_none(attrs[source])
        (MaxLengthValidator(64))(attrs[source])
        validate_not_white_space_padded(attrs[source])
        (MinLengthValidator(2))(attrs[source])
        return attrs

    def validate_resolution_x(self, attrs, source):
        """Validate resolution."""
        (IntegerValidator(minimum=20, maximum=1024*10))(attrs[source])
        return attrs

    def validate_resolution_y(self, attrs, source):
        """Validate resolution."""
        (IntegerValidator(minimum=20, maximum=1024*10))(attrs[source])
        return attrs

    def validate_pixel_density(self, attrs, source):
        """Validate pixel_density."""
        (IntegerValidator(minimum=1, maximum=1024*10))(attrs[source])
        return attrs

    def validate_adid(self, attrs, source):
        """Validate adid."""
        validate_device_adid(attrs[source])
        return attrs

    def validate_token(self, attrs, source):
        """Validate token."""
        validate_device_token(attrs[source])
        return attrs

    def validate_locale(self, attrs, source):
        """Validate locale."""
        validate_device_locale(attrs[source])
        return attrs

    def validate_time(self, attrs, source):
        """Validate time."""
        validate_device_time(attrs[source])
        return attrs

    def validate_tz(self, attrs, source):
        """Validate tz."""
        validate_device_tz(attrs[source])
        return attrs

    def validate_cpu(self, attrs, source):
        """Validate cpu."""
        (DecimalValidator(minimum=0, maximum=100))(attrs[source])
        return attrs

    def validate_battery_per(self, attrs, source):
        """Validate battery_per."""
        (DecimalValidator(minimum=0, maximum=100))(attrs[source])
        return attrs

    def validate_orientation(self, attrs, source):
        """Validate orientation."""
        if len(attrs[source]) > 9:
            raise ValidationError('String length greater than 8.')
        # TODO - Do not instantiate RegexValidator every time.
        if attrs[source] not in ('landscape', 'portrait'):
            raise ValidationError(
                'Valid value is either \'landscape\' or \'portrait\'.')
        return attrs

    def validate_orientation_deg(self, attrs, source):
        """Validate orientation_deg."""
        validate_device_orientation_deg(attrs[source])
        return attrs

    def validate_user_agent(self, attrs, source):
        """Validate user_agent."""
        validate_device_user_agent(attrs[source])
        return attrs
