"""TODO - Add doc."""


class FieldTestValues(object):

    """Helper class to maintain good, and bad values for a given field."""

    all_good_values = (None,)
    all_bad_values = (None,)

    @property
    def good_values(self):
        """Read-only tuple of good values."""
        return self.all_good_values

    @property
    def bad_values(self):
        """Read-only tuple of bad values."""
        return self.all_bad_values

    @property
    def good_value(self):
        """A known good value."""
        return self.all_good_values[0]

    @property
    def bad_value(self):
        """A known bad value."""
        return self.all_bad_values[0]


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


class DataGenerator(object):

    """Data generator, for use with FieldTestValues' children."""

    def __init__(self, data):
        """Create an instance of DataGenerator."""
        self.data = data

    def good_combination(self):
        """Return a dictionary with good vaules in all the fields."""
        good = {}
        for key in self.data.keys():
            good[key] = self.data[key].good_value
        return good

    def bad_combinations(self):
        """Return an array with bad data combinations for testing."""
        good_base_line = self.good_combination()
        combinations = []
        for key in self.data.keys():
            for bad_value in self.data[key].bad_values:
                bad_copy = good_base_line.copy()
                bad_copy[key] = bad_value
                combinations.append({
                    'data': bad_copy,
                    'expected_bad': set([key])})
        return combinations
