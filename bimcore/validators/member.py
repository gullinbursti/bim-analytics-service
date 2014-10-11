"""Common member data/field validators used in BIM."""

from __future__ import absolute_import
from bimcore.validators import validate_not_none, \
    validate_not_white_space_padded, validate_not_string, \
    ExactLengthValidator
from datetime import datetime
from django.core.exceptions import ValidationError

# from django.core.exceptions import ValidationError
from django.core.validators import validate_integer, MinValueValidator, \
    MinLengthValidator, MaxLengthValidator
# RegexValidator


def validate_member_id(value):
    """Validate that we have a valid member ID."""
    validate_not_none(value)
    validate_not_string(value)
    validate_integer(value)
    # TODO: Instantiate only once
    (MinValueValidator(1))(value)


def validate_member_name(value):
    """Validate that we have a valid member name."""
    # ALWAYS check max length first to minimize DOS attacks, after null check
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
    # ALWAYS check length first to minimize DOS attacks, after null check
    validate_not_none(value)
    # TODO: Seriously add a regex!!!
    (ExactLengthValidator(10))(value)
    try:
        datetime.strptime(value, r'%Y-%m-%d').date()
    except ValueError:
        raise ValidationError(
            'Does not match expected format of \'YYYY-MM-DD\', '
            'or values could be out of range.')


def validate_cohort_week(value):
    # TODO - Fix - pylint: disable=unused-argument
    """Validate that we have a valid member cohort week."""
    # ALWAYS check length first to minimize DOS attacks, after null check
    validate_not_none(value)
    # TODO: Seriously add a regex!!!
    (ExactLengthValidator(7))(value)
    try:
        datetime.strptime(value, r'%Y-%W').date()
    except ValueError:
        raise ValidationError(
            'Does not match expected format of \'YYYY-WW\', '
            'or values could be out of range.')
