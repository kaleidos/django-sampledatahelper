from django import models

class Register(object):
    fields = {}
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Register, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def register(self, field_class, method, *args, **kwargs)
        self.fields[field_class] = {
            "method": method,
            "args": *args,
            "kwargs": **kwargs,
        }

register = Register()

register.register(models.CharField, SampleDataHelper.paragraph, 1)
