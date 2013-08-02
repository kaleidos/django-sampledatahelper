class BaseHandler(object):
    def __init__(self, sd, instance):
        self.sd = sd
        self.instance = instance

    def generate(self):
        if self.instance.choices and len(self.instance.choices) > 0:
            return self.sd.choices_key(self.instance.choices)

        return self._generate()


class CharHandler(BaseHandler):
    def _generate(self):
        if self.instance.max_length < 10:
            return self.sd.chars(1, 10)
        elif self.instance.max_length < 50:
            return self.sd.words(1, 5)[0:self.instance.max_length]
        elif self.instance.max_length < 100:
            return self.sd.words(1, 10)[0:self.instance.max_length]
        elif self.instance.max_length < 200:
            return self.sd.short_sentence()[0:self.instance.max_length]
        else:
            return self.sd.long_sentence()[0:self.instance.max_length]


class SlugHandler(BaseHandler):
    def _generate(self):
        if self.instance.max_length < 10:
            return self.sd.chars(1, 10)
        elif self.instance.max_length < 50:
            return self.sd.slug(1, 5)[0:self.instance.max_length]
        elif self.instance.max_length < 100:
            return self.sd.slug(1, 10)[0:self.instance.max_length]
        elif self.instance.max_length < 200:
            return self.sd.slug(5, 15)[0:self.instance.max_length]
        else:
            return self.sd.slug(15, 25)[0:self.instance.max_length]


class EmailHandler(BaseHandler):
    def _generate(self):
        return self.sd.email()


class URLHandler(BaseHandler):
    def _generate(self):
        return self.sd.url()


class TextHandler(BaseHandler):
    def _generate(self):
        return self.sd.paragraphs(2, 5)


class IntegerHandler(BaseHandler):
    def _generate(self):
        return self.sd.int(-1000000, 1000000)


class SmallIntegerHandler(BaseHandler):
    def _generate(self):
        return self.sd.int(-32000, 32000)


class PositiveSmallIntegerHandler(BaseHandler):
    def _generate(self):
        return self.sd.int(0, 65000)


class PositiveIntegerHandler(BaseHandler):
    def _generate(self):
        return self.sd.int()


class BigIntegerHandler(IntegerHandler):
    pass


class DecimalHandler(IntegerHandler):
    pass


class FloatHandler(BaseHandler):
    def _generate(self):
        return self.sd.float(-1000000, 1000000)


class BooleanHandler(BaseHandler):
    def _generate(self):
        return self.sd.boolean()


class NullBooleanHandler(BaseHandler):
    def _generate(self):
        return self.sd.nullboolean()


class CommaSeparatedIntegerHandler(BaseHandler):
    def _generate(self):
        integers = []
        for x in range(self.sd.int(3, 8)):
            integers.append(str(self.sd.int(0, 1000)))

        return ",".join(integers)


class DateHandler(BaseHandler):
    def _generate(self):
        return self.sd.date()


class DateTimeHandler(BaseHandler):
    def _generate(self):
        return self.sd.datetime()


class TimeHandler(BaseHandler):
    def _generate(self):
        return self.sd.time()


class FileHandler(BaseHandler):
    def _generate(self):
        return self.sd.image(100, 100, 'random')


class FilePathHandler(BaseHandler):
    def _generate(self):
        return self.sd.path()


class ImageHandler(BaseHandler):
    def _generate(self):
        return self.sd.image(100, 100, 'random')


class IPAddressHandler(BaseHandler):
    def _generate(self):
        return self.sd.ipv4()


class GenericIPAddressHandler(BaseHandler):
    def _generate(self):
        if self.sd.boolean():
            return self.sd.ipv4()
        else:
            return self.sd.ipv6()


class ForeignKeyHandler(BaseHandler):
    def _generate(self):
        if self.instance.rel.limit_choices_to:
            queryset = self.instance.rel.to.objects.filter(**self.instance.rel.limit_choices_to)
        else:
            queryset = self.instance.rel.to.objects.all()
        return self.sd.db_object_from_queryset(queryset)


class OneToOneHandler(ForeignKeyHandler):
    def _generate(self):
        if self.instance.rel.limit_choices_to:
            queryset = self.instance.rel.to.objects.filter(
                **self.instance.rel.limit_choices_to
            ).exclude(id__in=self.instance.model.objects.all().values(self.instance.name))
        else:
            quersyet = self.instance.rel.to.objects.all()
            queryset = quersyet.exclude(id__in=self.instance.model.objects.all().values(self.instance.name))
        return self.sd.db_object_from_queryset(queryset)
