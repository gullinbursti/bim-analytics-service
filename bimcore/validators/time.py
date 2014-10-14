# -*- coding: utf-8 -*-
"""Time based validators."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError


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
