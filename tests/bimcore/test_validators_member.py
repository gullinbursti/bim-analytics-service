"""Tests for bimcore.validator.member."""

from __future__ import absolute_import
from bimcore.validators import member as mem_validators
from bimtest.values import member as testvalues
from django.core.exceptions import ValidationError
import pytest


@pytest.mark.parametrize(
    'bad_value',
    testvalues.MemberIdTestValues().bad_values)
def test_bad_values_for_validate_member_id(bad_value):
    """Test errors on all bad member ID values."""
    with pytest.raises(ValidationError):
        mem_validators.validate_member_id(bad_value)
