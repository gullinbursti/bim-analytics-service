"""BIM common validators."""

from __future__ import absolute_import

__all__ = ('IntegerValidator',
           'ExactLengthValidator',
           'validate_not_string',
           'validate_not_white_space_padded',
           'validate_not_none')

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.translation import ugettext_lazy
import sys


def validate_not_none(value):
    """Validate that the value is not None/Null."""
    if value is None:
        raise ValidationError('Value must not be Null/None.')


def validate_not_white_space_padded(value):
    """Validate that the value is padded with spaces."""
    if len(value) != len(value.strip()):
        raise ValidationError('Space padding not allowed.')


def validate_not_string(value):
    """Validate that the value is not a string."""
    if isinstance(value, str):
        raise ValidationError('String value not allowed.')


class ExactLengthValidator(BaseValidator):
    # Taken care of by BaseValidator pylint: disable=too-few-public-methods

    """Check exact length of a string."""

    compare = lambda self, a, b: a != b
    clean = lambda self, x: len(x)
    message = ugettext_lazy(
        'Ensure this value has exacty %(limit_value)d characters '
        '(it has %(show_value)d)')
    code = 'expected_length'


class IntegerValidator(object):
    # pylint: disable=too-few-public-methods

    """TODO something."""

    def __init__(self, minimum=(-sys.maxsize - 1), maximum=sys.maxsize):
        """Set minimum, and maximum values for integer."""
        self.minimum = minimum
        self.maximum = maximum

    def __call__(self, value):
        """Verify that integer is within range."""
        validate_not_string(value)
        if value > self.maximum or value < self.minimum:
            raise ValidationError(
                'Integer must be between {} and {}'.format(self.minimum,
                                                           self.maximum))
