"""Unit tests for the Selfieclub code validators."""

from __future__ import absolute_import
from bimcore import validators as bcvalidators
from bimtest.values import GuidTestValues, LocaleCodeTestValues
from django.core.exceptions import ValidationError
import pytest


# -----------------------------------------------------------------------------
# validate_guid()
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('bad_value', (GuidTestValues()).bad_values)
def test_bad_values_for_validate_guid(bad_value):
    """Test errors on all bad GUID values."""
    with pytest.raises(ValidationError):
        bcvalidators.validate_guid(bad_value)


@pytest.mark.parametrize('good_value', (GuidTestValues()).good_values)
def test_good_values_for_validate_guid(good_value):
    """Test all good GUID values."""
    bcvalidators.validate_guid(good_value)


# -----------------------------------------------------------------------------
# validate_locale_code()
# -----------------------------------------------------------------------------
@pytest.mark.parametrize('bad_value', (LocaleCodeTestValues()).bad_values)
def test_bad_values_for_validate_locale_code(bad_value):
    """Test errors on all bad locale code values."""
    with pytest.raises(ValidationError):
        bcvalidators.validate_locale_code(bad_value)


@pytest.mark.parametrize('good_value', (LocaleCodeTestValues()).good_values)
def test_good_values_for_validate_locale_code(good_value):
    """Test all good locale code values."""
    bcvalidators.validate_locale_code(good_value)
