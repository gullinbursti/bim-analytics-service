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
        )
    all_bad_values = (
        None,                 # Empty/false values
        0,                    # ^
        False,                # ^
        -1,                   # Negative
        'string',             # string
        '   ',                # ^
        '',                   # ^
        '  786',              # ^
        ' 786 ',              # ^
        '00786',              # ^
        (-sys.maxsize - 1),   # ^
        )


class MemberNameTestValues(FieldTestValues):

    """Contains test values for member names."""

    all_good_values = (
        'jerry',
        'aaa',           # Min size
        'a' * 255,       # Max size
        )
    all_bad_values = (
        None,
        '',
        '    ',
        '\t',
        'aa',            # Too small
        'a' * 256,       # Too large
        '   jerry',      # No white space padding
        'jerry ',        # ^
        ' jerry ',       # ^
        '\tjerry ',      # ^
        '\tjerry\t',     # ^
        '\njerry',       # ^
        '\njerry\n',     # ^
        )


class CohortDateTestValues(FieldTestValues):

    """Contains test values for cohort date."""

    all_good_values = (
        '2014-10-01',
        '0001-01-01',      # Minimum
        '9999-12-31',      # Maximum
        '2016-02-29',      # Leap day
        )
    all_bad_values = (
        None,
        '',
        '20141001',
        '2014-10-00',      # Day out of range, low
        '2014-10-32',      # Day out of range, high
        '2014-00-01',      # Month out of range, low
        '2014-13-01',      # Month out of range, high
        '0000-01-01',      # Year out of range, low
        '2015-02-29',      # Bad leap day
        ' 2014-10-01',     # Padding
        ' 2014-10-01 ',    # ^
        '2014-10-01 ',     # ^
        )


class CohortWeekTestValues(FieldTestValues):

    """Contains test values for cohort weeks."""

    all_good_values = (
        '2014-43',
        '0001-00',        # Minimum
        '9999-53',        # Maximum
        )
    all_bad_values = (
        None,
        '',
        '201443',
        '0000-43',       # Year too low
        '2014-54',       # Week too high
        ' 2014-43',      # Padding
        ' 2014-43 ',     # Padding
        '2014-43 ',      # Padding
        )
