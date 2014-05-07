from django.db import models
from sampledatahelper.helper import SampleDataHelper
from sampledatahelper import handlers


class Register(object):
    fields = {}
    ignored_fields = []
    _instance = None
    sd = SampleDataHelper()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Register, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def register(self, field_class, handler_class):
        self.fields[field_class] = handler_class

    def ignore(self, field_class):
        self.ignored_fields.append(field_class)

    def get_handler(self, field_instance):
        if field_instance.__class__ in self.ignored_fields:
            return None
        handler = self.fields.get(field_instance.__class__, None)
        if handler:
            return handler(self.sd, field_instance)
        return None


register = Register()
register.register(models.CharField, handlers.CharHandler)
register.register(models.BigIntegerField, handlers.BigIntegerHandler)
register.register(models.CharField, handlers.CharHandler)
register.register(models.SlugField, handlers.SlugHandler)
register.register(models.EmailField, handlers.EmailHandler)
register.register(models.URLField, handlers.URLHandler)
register.register(models.TextField, handlers.TextHandler)
register.register(models.IntegerField, handlers.IntegerHandler)
register.register(models.SmallIntegerField, handlers.SmallIntegerHandler)
register.register(models.PositiveIntegerField, handlers.PositiveIntegerHandler)
register.register(models.PositiveSmallIntegerField, handlers.PositiveSmallIntegerHandler)
register.register(models.BigIntegerField, handlers.BigIntegerHandler)
register.register(models.FloatField, handlers.FloatHandler)
register.register(models.BooleanField, handlers.BooleanHandler)
register.register(models.NullBooleanField, handlers.NullBooleanHandler)
register.register(models.CommaSeparatedIntegerField, handlers.CommaSeparatedIntegerHandler)
register.register(models.DecimalField, handlers.DecimalHandler)
register.register(models.DateField, handlers.DateHandler)
register.register(models.DateTimeField, handlers.DateTimeHandler)
register.register(models.TimeField, handlers.TimeHandler)
register.register(models.FileField, handlers.FileHandler)
register.register(models.FilePathField, handlers.FilePathHandler)
register.register(models.ImageField, handlers.ImageHandler)
register.register(models.IPAddressField, handlers.IPAddressHandler)
register.register(models.GenericIPAddressField, handlers.GenericIPAddressHandler)
register.register(models.ForeignKey, handlers.ForeignKeyHandler)
register.register(models.OneToOneField, handlers.OneToOneHandler)
register.ignore(models.ManyToManyField)
register.ignore(models.AutoField)
