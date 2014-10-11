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


@pytest.mark.parametrize(
    'good_value',
    testvalues.MemberIdTestValues().good_values)
def test_good_values_for_validate_member_id(good_value):
    """Test errors on all good member ID values."""
    mem_validators.validate_member_id(good_value)


@pytest.mark.parametrize(
    'bad_value',
    testvalues.MemberNameTestValues().bad_values)
def test_bad_values_for_validate_member_name(bad_value):
    """Test errors on all bad member names values."""
    with pytest.raises(ValidationError):
        mem_validators.validate_member_name(bad_value)


@pytest.mark.parametrize(
    'good_value',
    testvalues.MemberNameTestValues().good_values)
def test_good_values_for_validate_member_name(good_value):
    """Test errors on all good member names values."""
    mem_validators.validate_member_name(good_value)


@pytest.mark.parametrize(
    'bad_value',
    testvalues.CohortDateTestValues().bad_values)
def test_bad_values_for_validate_cohort_date(bad_value):
    """Test errors on all bad cohort date values."""
    with pytest.raises(ValidationError):
        mem_validators.validate_cohort_date(bad_value)


@pytest.mark.parametrize(
    'good_value',
    testvalues.CohortDateTestValues().good_values)
def test_good_values_for_validate_cohort_date(good_value):
    """Test errors on all good cohort date values."""
    mem_validators.validate_cohort_date(good_value)


@pytest.mark.parametrize(
    'bad_value',
    testvalues.CohortWeekTestValues().bad_values)
def test_bad_values_for_validate_cohort_week(bad_value):
    """Test errors on all bad cohort week values."""
    with pytest.raises(ValidationError):
        mem_validators.validate_cohort_week(bad_value)


@pytest.mark.parametrize(
    'good_value',
    testvalues.CohortWeekTestValues().good_values)
def test_good_values_for_validate_cohort_week(good_value):
    """Test errors on all good cohort week values."""
    mem_validators.validate_cohort_week(good_value)
