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
