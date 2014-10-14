"""Field test data helpers."""

from __future__ import absolute_import

__all__ = ('FieldTestValues',
           'DataGenerator',
           'GuidTestValues',
           'LocaleCodeTestValues')


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


class GuidTestValues(FieldTestValues):

    """Contains test values for GUIDs."""

    all_good_values = (
        'DBE8FCC9-5341-43F7-B30A-6F7E6893243F',
        '5D844F1C-11D9-4696-B7C1-79412B3E4A12',
        'C881DCFE-48A5-4B1E-80B2-A00FF862D759',
        '3D0A67AB-8C58-4C3C-87BA-077C015585B9',
        'C71961C7-BD15-4F60-AFC4-80E085780789',
        '1F52C3B4-7AFC-4F80-A7BC-65C473D8B6AF',
        'D2098FEE-D09C-4844-B0DD-B4A9705FAC7D',
        )
    all_bad_values = (
        None,
        '',
        ' '*36,
        '3d103ca0-367e-4028-9a55-9e88ed2eb1a3',              # all lower
        '02dE4D17-AD5B-494D-B15F-54C397C93F41',              # one lower
        '02DE4D17AD5B494DB15F54C397C93F41',                  # missing dash (-)
        '{8D9B8FB8-8B0B-4453-B4A0-F2A2D799A824}',            # with curlies
        '\n3005E60A-5711-416C-BDC6-EFCF9640B1C1',            # padding
        '\t3005E60A-5711-416C-BDC6-EFCF9640B1C1',            # ^
        ' 3005E60A-5711-416C-BDC6-EFCF9640B1C1 ',            # ^
        '3005E60A-5711-416C-BDC6-EFCF9640B1C1EFCF9640B1C1',  # too long
        )


class LocaleCodeTestValues(FieldTestValues):

    """Contains test values locale codes."""

    # Pulled from: https://gist.github.com/jacobbubu/1836273
    all_good_values = (
        'mr', 'bs', 'ee_tg', 'ms', 'kam_ke', 'mt', 'ha', 'es_hn', 'ml_in',
        'ro_md', 'kab_dz', 'he', 'es_co', 'my', 'es_pa', 'az_latn', 'mer',
        'en_nz', 'xog_ug', 'sg', 'fr_gp', 'sr_cyrl_ba', 'hi', 'fil_ph',
        'lt_lt', 'si', 'en_mt', 'si_lk', 'luo_ke', 'it_ch', 'teo', 'mfe', 'sk',
        'uz_cyrl_uz', 'sl', 'rm_ch', 'az_cyrl_az', 'fr_gq', 'kde', 'sn',
        'cgg_ug', 'es_419', 'so', 'a'*32)
    all_bad_values = (
        None,
        '',
        'g'*33,            # too long
        'CGG_UG',          # upper case
        '  en_us',         # padded
        'en_us ',          # ^
        'en_us ',          # ^
        '   en_us ',       # ^
        '\ten_us',         # ^
        '\ren_us',         # ^
        )
