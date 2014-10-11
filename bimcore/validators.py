"""Common data/field validators used in BIM."""

from __future__ import absolute_import

# from django.core.exceptions import ValidationError
from django.core.validators import validate_integer, MinValueValidator


def validate_member_id(value):
    """Validate that we have a valid member ID."""
    validate_integer(value)
    (MinValueValidator(1))(value)
