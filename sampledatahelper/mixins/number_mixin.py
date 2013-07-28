import sys
import random

from ..exceptions import ParameterError


class NumberMixin(object):
    def int(self, min_value=0, max_value=sys.maxsize):
        """Random number from 0 or min_value to max_value - 1 or sys.maxint - 1."""

        if min_value > max_value:
            raise ParameterError('min_value greater than max_value')

        return random.randrange(min_value, max_value + 1)

    def number(self, ndigits):
        """Random number with the given number of digits as maximum."""

        if ndigits < 1:
            raise ParameterError('ndigits is less than 1')

        return random.randrange(0, 10 ** ndigits)

    def digits(self, ndigits):
        """Random number with exactly the given number of digits."""
        if ndigits < 1:
            raise ParameterError('ndigits is less than 1')

        return random.randrange(10 ** (ndigits-1), 10 ** ndigits)

    def float(self, min_value, max_value):
        """Random float from min to max"""

        if min_value > max_value:
            raise ParameterError('min_value greater than max_value')

        return (max_value - (random.random() * (max_value - min_value)))

    def number_string(self, ndigits):
        """Random number from 0 to ndigits, in string format, filled by 0s on the left."""

        if ndigits < 0:
            raise ParameterError('ndigits is less than 0')

        return u''.join(random.choice(u'0123456789') for i in range(ndigits))
