import random


class OtherMixin(object):
    def boolean(self):
        return random.randrange(0, 2) == 0

    def choice(self, choices):
        return random.choice(choices)

    def choices_key(self, choices):
        try:
            return self.choice(choices)[0]
        except ValueError:
            return None

    def db_object(self, model):
        return self.db_object_from_queryset(model.objects.all())

    def db_object_from_queryset(self, queryset):
        count = queryset.all().count()
        return queryset.all()[self.int(max_value=count)] if count > 0 else None
