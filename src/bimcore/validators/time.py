# -*- coding: utf-8 -*-
"""Time based validators."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
from bimcore.validators import ExactLengthValidator, validate_is_string
from datetime import datetime


UTC_OFFSETS = (
    u'UTC-12:00', u'UTC-11:00', u'UTC-10:00', u'UTC-09:30', u'UTC-09:00',
    u'UTC-08:00', u'UTC-07:00', u'UTC-06:00', u'UTC-05:00', u'UTC-04:30',
    u'UTC-04:00', u'UTC-03:30', u'UTC-03:00', u'UTC-02:00', u'UTC-01:00',
    u'UTC±00:00', u'UTC+01:00', u'UTC+02:00', u'UTC+03:00', u'UTC+03:30',
    u'UTC+04:00', u'UTC+04:30', u'UTC+05:00', u'UTC+05:30', u'UTC+05:45',
    u'UTC+06:00', u'UTC+06:30', u'UTC+07:00', u'UTC+08:00', u'UTC+08:45',
    u'UTC+09:00', u'UTC+09:30', u'UTC+10:00', u'UTC+10:30', u'UTC+11:00',
    u'UTC+11:30', u'UTC+12:00', u'UTC+12:45', u'UTC+13:00', u'UTC+14:00')


def validate_utc_offset(value):
    u"""Validate timezone provided as a UTC offset.

    UTC offset is expected to be in the form of 'UTC±HH:MM'.

    Reffer to the following for more information:
        http://en.wikipedia.org/wiki/UTC_offset
    """
    if value not in UTC_OFFSETS:
        raise ValidationError('Unknown UTC offset.  Expects \'UTC±HH:MM\'.')


def validate_utc_iso8601(value):
    """Validate date time in UTC ISO 8601 format.

    Time must be in at/on UTC.  Only the following form is allowed:
        2014-10-13T15:09:10Z
    """
    validate_is_string(value)
    (ExactLengthValidator(20))(value)
    try:
        datetime.strptime(value, r'%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        raise ValidationError(
            'Datetime expected to be in \'YYYY-MM-DDThh:mm:ssZ\'.')
