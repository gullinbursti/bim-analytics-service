"""Member related field data to test with."""

from __future__ import absolute_import
from bimtest.values import FieldTestValues
import sys


class MemberIdTestValues(FieldTestValues):

    """Contains test values for member IDs."""

    all_good_values = (
        1,
        12893,
        sys.maxsize,
        '  786',              # Number as a string, space padded
        ' 786 ',              # Number as a string, space padded
        '00786',              # Number as a string, zero  padded
        )
    all_bad_values = (
        None,                 # Empty/false values
        0,                    # ^
        False,                # ^
        -1,                   # Negative
        'string',             # string
        '   ',                # spaces
        '',                   # Empty string
        (-sys.maxsize - 1),   # Smallest integer
        )


class MemberNameTestValues(FieldTestValues):

    """Contains test values for member names."""

    all_good_values = (
        'jerry',)
    all_bad_values = (
        None,
        '',)


class CohortDateTestValues(FieldTestValues):

    """Contains test values for cohort date."""

    all_good_values = (
        '2014-10-01',)
    all_bad_values = (
        None,
        '',)


class CohortWeekTestValues(FieldTestValues):

    """Contains test values for cohort weeks."""

    all_good_values = (
        '2014-43',)
    all_bad_values = (
        None,
        '',)
