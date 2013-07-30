import random

from ..exceptions import ParameterError


class OtherMixin(object):
    def boolean(self):
        return random.randrange(0, 2) == 0

    def nullboolean(self):
        return random.choice([None, True, False])

    def choice(self, choices):
        if not isinstance(choices, list) and not isinstance(choices, tuple):
            raise ParameterError('choices must be a list or a tuple')

        if choices == []:
            raise ParameterError('choices can\'t be a empty list')

        return random.choice(choices)

    def choices_key(self, choices):
        if not isinstance(choices, list) and not isinstance(choices, tuple):
            raise ParameterError('choices must be a list or a tuple')

        try:
            return self.choice(choices)[0]
        except (TypeError, ValueError, ParameterError):
            raise ParameterError('choices must be a valid django choices list')

    def db_object(self, model):
        return self.db_object_from_queryset(model.objects.all())

    def db_object_from_queryset(self, queryset):
        count = queryset.all().count()
        return queryset.all()[self.int(max_value=count)] if count > 0 else None

    def ipv4(self):
        return "{0}.{1}.{2}.{3}".format(
            self.int(0, 255),
            self.int(0, 255),
            self.int(0, 255),
            self.int(0, 255),
        )

    def ipv6(self):
        return "{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}".format(
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4)
        )

    def hex_chars(self, min_chars, max_chars):
        result = ""
        for x in range(min_chars, max_chars + 1):
            result += self.choice(['0', '1','2', '3', '4', '5', '6', '7',
                                      '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'])
        return result

    def path(self, absolute=None, extension='', min_levels=1, max_levels=5):
        if absolute is None:
            absolute = self.boolean()

        if absolute:
            result = "/"
        else:
            result = ""

        for x in range(min_levels, max_levels + 1):
            result += self.word()
            if x != max_levels:
                result += "/"

        result != extension

        return result
