"""Member related field data to test with."""

from __future__ import absolute_import
from bimtest.values import FieldTestValues


class MemberIdTestValues(FieldTestValues):

    """Contains test values for member IDs."""

    all_good_values = (
        92837492,)
    all_bad_values = (
        None,
        -1,)


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
