"""Selfieclub event serializers."""

from __future__ import absolute_import
from . import dtos
from bimcore.validators import IntegerValidator, DecimalValidator, \
    ExactLengthValidator
from bimcore.validators.analytics.device import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import
from bimcore.validators.member import validate_cohort_date
from bimcore.validators.member import validate_cohort_week
from bimcore.validators.member import validate_member_id
from bimcore.validators.member import validate_member_name
from bimcore.validators.time import validate_utc_offset, validate_utc_iso8601
from bimcore.validators import validate_not_white_space_padded, \
    validate_not_none, validate_guid, validate_locale_code
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, \
    RegexValidator
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
            identifier=attrs['id'],
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
    orientation_deg = serializers.IntegerField(required=True)
    platform = serializers.CharField(required=True)
    platform_version = serializers.CharField(required=True)
    resolution_x = serializers.IntegerField(required=True)
    resolution_y = serializers.IntegerField(required=True)
    time = serializers.CharField(required=True)
    timezone = serializers.CharField(required=True)
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
            platform=attrs['platform'],
            platform_version=attrs['platform_version'],
            resolution_x=attrs['resolution_x'],
            resolution_y=attrs['resolution_y'],
            time=attrs['time'],
            timezone=attrs['timezone'],
            user_agent=attrs['user_agent'])

    def validate_platform(self, attrs, source):
        """Validate platform."""
        if len(attrs[source]) > 8:
            raise ValidationError('String length greater than 8.')
        if attrs[source] not in ('ios', 'android'):
            raise ValidationError(
                'Valid value is either \'ios\' or \'android\'.')
        return attrs

    def validate_platform_version(self, attrs, source):
        """Validate platform_version."""
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
        validate_guid(attrs[source])
        return attrs

    def validate_locale(self, attrs, source):
        """Validate locale."""
        validate_locale_code(attrs[source])
        return attrs

    def validate_time(self, attrs, source):
        """Validate time."""
        validate_utc_iso8601(attrs[source])
        return attrs

    def validate_timezone(self, attrs, source):
        """Validate UTC offset for timezone."""
        validate_utc_offset(attrs[source])
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
        if attrs[source] not in (0, 90, 180, 270):
            raise ValidationError('Value must be one of: 0, 90, 180, 270')
        return attrs

    def validate_user_agent(self, attrs, source):
        """Validate user_agent."""
        validate_not_none(attrs[source])
        (MaxLengthValidator(2048))(attrs[source])
        validate_not_white_space_padded(attrs[source])
        return attrs


class StateInfoSerializer(serializers.Serializer):
    # pylint: disable=too-few-public-methods, star-args

    """Used to track actions and screen states."""

    _common_config = {
        'required': True,
        'max_length': 32,
        'min_length': 4,
        'validators': [
            validate_not_white_space_padded,
            RegexValidator(
                regex=r'^[A-Z0-9_\-]{4,32}$',
                message=r'Must be in the form of \'^[A-Z0-9_\-]{4,32}$\'',
                code='invalid_state_info_state')]
    }

    screen_current = serializers.CharField(**(_common_config.copy()))
    screen_previous = serializers.CharField(**(_common_config.copy()))
    action_current = serializers.CharField(**(_common_config.copy()))
    action_previous = serializers.CharField(**(_common_config.copy()))


class ApplicationSerializer(serializers.Serializer):
    # pylint: disable=too-few-public-methods, star-args

    """Used to track actions and screen states."""

    _common_config = {
        'required': True,
        'max_length': 32,
        'min_length': 4,
        'validators': [
            validate_not_white_space_padded,
            RegexValidator(
                regex=r'^[a-z0-9_\-\.]{4,32}$',
                message=r'Must be in the form of \'^[a-z0-9_\-\.]{4,32}$\'',
                code='invalid_version_string')]
    }

    client_version = serializers.CharField(**(_common_config.copy()))
    service_selfieclub_version \
        = serializers.CharField(**(_common_config.copy()))
    service_bimanalytics_version \
        = serializers.CharField(**(_common_config.copy()))
    service_volley_version = serializers.CharField(
        validators=[
            ExactLengthValidator(6),
            validate_not_white_space_padded,
            RegexValidator(
                regex=r'^sc[0-9]{4}$',
                message=r'Must be in the form of \'^sc[0-9]{4}$\'',
                code='invalid_version_string')])
    service_env = serializers.CharField(
        required=True,
        max_length=6,
        min_length=4,
        validators=[
            validate_not_white_space_padded,
            RegexValidator(
                regex=r'^(devint|prod)$',
                message=r'Must be in the form of \'^(devint|prod)\'',
                code='invalid_version_string')])


class AnalyticsEventSerializer(serializers.Serializer):
    # pylint: disable=too-few-public-methods, no-value-for-parameter
    # pylint: disable=unexpected-keyword-arg, no-self-use

    """Analytics event serializer."""

    device = DeviceSerializer(required=True)
    member = MemberSerializer(required=True)
    state_info = StateInfoSerializer(required=True)
    application = ApplicationSerializer(required=True)

    def validate_device(self, attrs, source):
        """Validate device."""
        validate_not_none(attrs[source])
        return attrs

    def validate_member(self, attrs, source):
        """Validate device."""
        validate_not_none(attrs[source])
        return attrs

    def validate_state_info(self, attrs, source):
        """Validate device."""
        validate_not_none(attrs[source])
        return attrs

    def validate_application(self, attrs, source):
        """Validate application."""
        validate_not_none(attrs[source])
        return attrs
