"""BIM common validators."""

from __future__ import absolute_import

__all__ = ('DecimalValidator',
           'IntegerValidator',
           'ExactLengthValidator',
           'validate_guid',
           'validate_locale_code',
           'validate_not_string',
           'validate_not_white_space_padded',
           'validate_not_none')

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator, RegexValidator, \
    MaxLengthValidator
from django.utils.translation import ugettext_lazy
import sys
from decimal import Decimal


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


def validate_guid(value):
    """Validate that we have a valid GUID.

    GUIDs are expected to be in the form of:
        F53137B7-8220-4F20-A45D-C9D30F87A601

    Note that all caps is manditory.
    """
    validate_not_none(value)
    (ExactLengthValidator(36))(value)
    regex = r'^[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}$'
    (RegexValidator(
        regex=regex,
        message='GUID must be all caps, and in the form of: '
                'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'))(value)


def validate_locale_code(value):
    """Validate locale.

    Should be in the form of 'en_us'.
    """
    validate_not_none(value)
    (MaxLengthValidator(32))(value)
    (RegexValidator(
        regex=r'^[a-z0-9_]+$',
        message='Locale expected to be either \'xx\', or \'xx_yy\''))(value)


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

    """Validate integer and make sure it is within range."""

    def __init__(self, minimum=(-sys.maxsize - 1), maximum=sys.maxsize):
        """Set minimum, and maximum values for integer."""
        self.minimum = minimum
        self.maximum = maximum

    def __call__(self, value):
        """Verify that integer is within range."""
        validate_not_string(value)
        try:
            int(value)
        except ValueError:
            raise ValidationError('Integer was expected.')

        if value > self.maximum or value < self.minimum:
            raise ValidationError(
                'Integer must be between {} and {}'.format(self.minimum,
                                                           self.maximum))


class DecimalValidator(object):
    # pylint: disable=too-few-public-methods

    """Validate decimal and make sure that it is within range."""

    def __init__(self, minimum=None, maximum=None):
        """Set minimum, and maximum values for decimal."""
        self.minimum = minimum
        self.maximum = maximum

    def __call__(self, value):
        """Verify that decimal is within range."""
        validate_not_string(value)
        try:
            Decimal(value)
        except ValueError:
            raise ValidationError('Decimaling point number expected.')

        if self.maximum is not None and value > self.maximum:
            raise ValidationError(
                'Decimal must be between less than {}'.format(self.maximum))
        if self.minimum is not None and value < self.minimum:
            raise ValidationError(
                'Decimal must be between greater than {}'.format(self.minimum))
