"""BIM common validators."""

from __future__ import absolute_import
from django.core.exceptions import ValidationError
# from django.core.validators import BaseValidator


def validate_not_none(value):
    """Validate that the value is not None/Null."""
    if value is None:
        raise ValidationError('Value must not be Null/None.')


def validate_not_white_space_padded(value):
    """Validate that the value is padded with spaces."""
    if len(value) != len(value.strip()):
        raise ValidationError('Space padding not allowed.')
