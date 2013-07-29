class BaseHandler(object):
    def __init__(self, sd, instance):
        self.sd = sd
        self.instance = instance

    def generate(self):
        if self.instance.choices and len(self.instance.choices) > 0:
            return self.sd.choices_key(self.instance.choices)

class CharHandler(BaseHandler):
    def generate(self):
        value = super(CharHandler, self).generate()
        if value:
            return value

        if self.instance.max_length < 10:
            return self.sd.chars(1, 10)
        elif self.instance.max_length < 50:
            return self.sd.words(1, 5)[0:self.instance.max_length]
        elif self.instance.max_length < 100:
            return self.sd.words(1, 10)[0:self.instance.max_length]
        elif self.instance.max_length < 200:
            return self.sd.short_sentence()
        elif self.instance.max_length < 250:
            return self.sd.long_sentence()

class SlugHandler(BaseHandler):
    def generate(self):
        value = super(SlugHandler, self).generate()
        if value:
            return value

        if self.instance.max_length < 10:
            return self.sd.chars(1, 10)
        elif self.instance.max_length < 50:
            return self.sd.slug(1, 5)[0:self.instance.max_length]
        elif self.instance.max_length < 100:
            return self.sd.slug(1, 10)[0:self.instance.max_length]
        elif self.instance.max_length < 200:
            return self.sd.slug(5, 15)[0:self.instance.max_length]
        elif self.instance.max_length < 250:
            return self.sd.slug(15, 25)[0:self.instance.max_length]

class EmailHandler(BaseHandler):
    def generate(self):
        value = super(EmailHandler, self).generate()
        if value:
            return value

        return self.sd.email()

class URLHandler(BaseHandler):
    def generate(self):
        value = super(URLHandler, self).generate()
        if value:
            return value

        return self.sd.url()

class TextHandler(BaseHandler):
    def generate(self):
        value = super(TextHandler, self).generate()
        if value:
            return value

        return self.sd.paragraphs(2, 5)

class IntegerHandler(BaseHandler):
    def generate(self):
        value = super(IntegerHandler, self).generate()
        if value:
            return value

        return self.sd.int(-1000000, 1000000)

class SmallIntegerHandler(BaseHandler):
    def generate(self):
        value = super(SmallIntegerHandler, self).generate()
        if value:
            return value

        return self.sd.int(-32000, 32000)

class PositiveSmallIntegerHandler(BaseHandler):
    def generate(self):
        value = super(PositiveSmallIntegerHandler, self).generate()
        if value:
            return value

        return self.sd.int(0, 65000)


class PositiveIntegerHandler(BaseHandler):
    def generate(self):
        value = super(PositiveIntegerHandler, self).generate()
        if value:
            return value

        return self.sd.int()


class BigIntegerHandler(IntegerHandler):
    pass


class DecimalHandler(IntegerHandler):
    pass

class FloatHandler(BaseHandler):
    def generate(self):
        value = super(FloatHandler, self).generate()
        if value:
            return value

        return self.sd.float(-1000000, 1000000)

class BooleanHandler(BaseHandler):
    def generate(self):
        value = super(BooleanHandler, self).generate()
        if value:
            return value

        return self.sd.boolean()

class NullBooleanHandler(BaseHandler):
    def generate(self):
        value = super(NullBooleanHandler, self).generate()
        if value:
            return value

        return self.sd.nullboolean()

class CommaSeparatedIntegerHandler(BaseHandler):
    pass

class DateHandler(BaseHandler):
    pass

class DateTimeHandler(BaseHandler):
    pass

class TimeHandler(BaseHandler):
    pass

class FileHandler(BaseHandler):
    pass

class FilePathHandler(BaseHandler):
    pass

class ImageHandler(BaseHandler):
    pass

class IPAddressHandler(BaseHandler):
    pass

class GenericIPAddressHandler(BaseHandler):
    pass

class ForeignKeyHandler(BaseHandler):
    pass

class OneToOneHandler(BaseHandler):
    pass

class ManyToManyHandler(BaseHandler):
    pass

