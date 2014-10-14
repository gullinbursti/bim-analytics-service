# -*- coding: utf-8 -*-
"""Time related test values."""

from __future__ import absolute_import
from bimtest.values import FieldTestValues


class UtcOffsetTestValues(FieldTestValues):

    """Contains test values for member IDs."""

    all_good_values = (
        u'UTC-12:00', u'UTC-08:00', u'UTC-03:30', u'UTC±00:00', u'UTC+04:00',
        u'UTC+09:30', u'UTC+12:45', u'UTC+14:00')
    all_bad_values = (
        None,                 # empty/false values
        0,                    # ^
        '',                   # ^
        False,                # ^
        -1,                   # Negative
        'string',             # string
        '   ',                # ^
        'utc-08:00',          # lower case
        u'UTC±06:00',         # non-existant
        )


class UtcIso8610TestValues(FieldTestValues):

    """Contains test values for member IDs."""

    all_good_values = (
        '2014-10-13T15:09:10Z',
        '2000-01-01T00:00:00Z',
        '0001-01-01T00:00:00Z',
        '9999-12-31T23:59:59Z',
        )
    all_bad_values = (
        None,                 # empty/false values
        0,                    # ^
        '',                   # ^
        False,                # ^
        -1,                   # negative
        'string',             # junk
        '   ',                # ^
        'utc-08:00',          # lower case
        u'UTC±06:00',         # non-existant
        '2000-13-13T15:09:10Z',  # bad month
        '2014-00-13T15:09:10Z',  # ^
        '2014-10-00T15:09:10Z',  # bad day
        '2014-10-32T15:09:10Z',  # ^
        '2014-10-13T24:00:00Z',  # bad hour
        '2014-10-13T23:60:00Z',  # bad minute
        '2014-10-13T23:00:60Z',  # bad second
        )
