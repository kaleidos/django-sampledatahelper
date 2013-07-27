import random

from ..exceptions import ParameterError


class OtherMixin(object):
    def boolean(self):
        return random.randrange(0, 2) == 0

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
