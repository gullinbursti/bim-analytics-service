"""Common member data/field validators used in BIM."""

from __future__ import absolute_import
from bimcore.validators import validate_not_none, \
    validate_not_white_space_padded

# from django.core.exceptions import ValidationError
from django.core.validators import validate_integer, MinValueValidator, \
    MinLengthValidator, MaxLengthValidator
# RegexValidator


def validate_member_id(value):
    """Validate that we have a valid member ID."""
    validate_integer(value)
    # TODO: Instantiate only once
    (MinValueValidator(1))(value)


def validate_member_name(value):
    """Validate that we have a valid member name."""
    # ALWAYS check max length first to minimize DOS attacks
    validate_not_none(value)
    # TODO: Instantiate only once
    (MaxLengthValidator(255))(value)
    (MinLengthValidator(3))(value)
    validate_not_white_space_padded(value)
    # TODO: Seriously add a regex!!!
    # (RegexValidator('^$'))(value)


def validate_cohort_date(value):
    # TODO - Fix - pylint: disable=unused-argument
    """Validate that we have a valid member cohort date."""
    # ALWAYS check max length first to minimize DOS attacks
    pass


def validate_cohort_week(value):
    # TODO - Fix - pylint: disable=unused-argument
    """Validate that we have a valid member cohort week."""
    # ALWAYS check max length first to minimize DOS attacks
    pass
