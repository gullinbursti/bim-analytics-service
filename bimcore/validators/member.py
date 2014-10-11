"""Common member data/field validators used in BIM."""

from __future__ import absolute_import

# from django.core.exceptions import ValidationError
from django.core.validators import validate_integer, MinValueValidator


def validate_member_id(value):
    """Validate that we have a valid member ID."""
    validate_integer(value)
    (MinValueValidator(1))(value)


def validate_cohort_date(value):
    # TODO - Fix - pylint: disable=unused-argument
    """Validate that we have a valid member cohort date."""
    pass


def validate_cohort_week(value):
    # TODO - Fix - pylint: disable=unused-argument
    """Validate that we have a valid member cohort week."""
    pass


def validate_member_name(value):
    # TODO - Fix - pylint: disable=unused-argument
    """Validate that we have a valid member name."""
    pass
