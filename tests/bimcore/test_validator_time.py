"""Test BIM core time validation functions."""

from __future__ import absolute_import
from bimcore.validators.time import validate_utc_offset
from bimtest.values.time import UtcOffsetTestValues
from django.core.exceptions import ValidationError
import pytest


@pytest.mark.parametrize('bad_value', (UtcOffsetTestValues()).bad_values)
def test_bad_values_for_validate_utc_offset(bad_value):
    """Test errors on all bad GUID values."""
    with pytest.raises(ValidationError):
        validate_utc_offset(bad_value)


@pytest.mark.parametrize('good_value', (UtcOffsetTestValues()).good_values)
def test_good_values_for_validate_utc_offset(good_value):
    """Test errors on all good GUID values."""
    validate_utc_offset(good_value)
