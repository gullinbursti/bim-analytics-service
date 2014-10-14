"""Test BIM core time validation functions."""

from __future__ import absolute_import
from bimcore.validators.time import validate_utc_offset, validate_utc_iso8601
from bimtest.values.time import UtcOffsetTestValues, UtcIso8610TestValues
from django.core.exceptions import ValidationError
import pytest


# -----------------------------------------------------------------------------
# validate_utc_offset()
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('bad_value', (UtcOffsetTestValues()).bad_values)
def test_bad_values_for_validate_utc_offset(bad_value):
    """Test errors on all bad GUID values."""
    with pytest.raises(ValidationError):
        validate_utc_offset(bad_value)


@pytest.mark.parametrize('good_value', (UtcOffsetTestValues()).good_values)
def test_good_values_for_validate_utc_offset(good_value):
    """Test errors on all good GUID values."""
    validate_utc_offset(good_value)


# -----------------------------------------------------------------------------
# validate_utc_iso8601()
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('bad_value', (UtcIso8610TestValues()).bad_values)
def test_bad_values_for_validate_utc_iso8601(bad_value):
    """Test errors on all bad GUID values."""
    with pytest.raises(ValidationError):
        validate_utc_iso8601(bad_value)


@pytest.mark.parametrize('good_value', (UtcIso8610TestValues()).good_values)
def test_good_values_for_validate_utc_iso8601(good_value):
    """Test errors on all good GUID values."""
    validate_utc_iso8601(good_value)
