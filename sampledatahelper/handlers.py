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
    pass

class EmailHandler(BaseHandler):
    pass

class URLHandler(BaseHandler):
    pass

class TextHandler(BaseHandler):
    pass

class IntegerHandler(BaseHandler):
    pass

class SmallIntegerHandler(BaseHandler):
    pass

class PositiveIntegerHandler(BaseHandler):
    pass

class PositiveSmallIntegerHandler(BaseHandler):
    pass

class BigIntegerHandler(BaseHandler):
    pass

class FloatHandler(BaseHandler):
    pass

class BooleanHandler(BaseHandler):
    pass

class NullBooleanHandler(BaseHandler):
    pass

class CommaSeparatedIntegerHandler(BaseHandler):
    pass

class DecimalHandler(BaseHandler):
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

