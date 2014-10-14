"""Unit tests for the Selfieclub code validators."""

from __future__ import absolute_import
from bimcore import validators as bcvalidators
from bimtest.values import GuidTestValues
from django.core.exceptions import ValidationError
import pytest


@pytest.mark.parametrize('bad_value', (GuidTestValues()).bad_values)
def test_bad_values_for_validate_guid(bad_value):
    """Test errors on all bad GUID values."""
    with pytest.raises(ValidationError):
        bcvalidators.validate_guid(bad_value)


@pytest.mark.parametrize('good_value', (GuidTestValues()).good_values)
def test_good_values_for_validate_guid(good_value):
    """Test errors on all good GUID values."""
    bcvalidators.validate_guid(good_value)
