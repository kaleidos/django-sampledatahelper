import sys
import random


class NumberMixin(object):
    def int(self, *args, **kwargs):
        """Random number from 0 or min_value to max_value - 1 or sys.maxint - 1."""
        if len(kwargs.keys()) > 0:
            min_value = 0
            max_value = sys.maxint
            if 'min_value' in kwargs.keys():
                min_value = kwargs['min_value']
            if 'max_value' in kwargs.keys():
                max_value = kwargs['max_value']
        else:
            if len(args) == 0:
                min_value = 0
                max_value = sys.maxint
            elif len(args) == 1:
                min_value = 0
                max_value = args[0]
            else:
                min_value = args[0]
                max_value = args[1]
        return random.randrange(min_value, max_value)

    def number(self, ndigits):
        """Random number with the given number of digits as maximum."""
        return random.randrange(0, 10 ** ndigits)

    def digits(self, ndigits):
        """Random number with exactly the given number of digits."""
        return random.randrange(10 ** (ndigits-1), 10 ** ndigits)

    def float(self, min, max):
        """Random float from min to max"""
        return (max - (random.random() * (max - min)))

    def number_string(self, ndigits):
        """Random number from 0 to ndigits, in string format, filled by 0s on the left."""
        return u''.join(random.choice(u'0123456789') for i in range(ndigits))
