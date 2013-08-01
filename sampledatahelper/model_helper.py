from django.db import models
from django.db.models.fields import FieldDoesNotExist

from .helper import SampleDataHelper
from .exceptions import ParameterError
from .register import register

class ModelDataHelper(object):
    def __init__(self, seed=None):
        self.sd = SampleDataHelper(seed)

    def __get_instance_fields(self, instance):
        fields = []
        for field_name in instance._meta.get_all_field_names():
            try:
                fields.append((field_name, instance._meta.get_field(field_name)))
            except FieldDoesNotExist:
                pass
        return fields

    def fill_model(self, model, number, **kwargs):
        if number <= 0:
            raise ParameterError('number must be greater than 0')

        if not issubclass(model, models.Model):
            raise ParameterError('model must be a django model subclass')

        for x in range(number):
            instance = model()
            self.fill_model_instance(instance, **kwargs)
            instance.save()

    def fill_model_instance(self, instance, **kwargs):
        if not isinstance(instance, models.Model):
            raise ParameterError('instance must be a django model instance')

        for field in self.__get_instance_fields(instance):
            field_name = field[0]
            field_obj = field[1]

            if field_name in kwargs:
                if hasattr(kwargs[field_name], '__call__'):
                    value = kwargs[field_name](instance, self.sd)
                else:
                    value = kwargs[field_name]
                setattr(instance, field_name, value)
            else:
                handler = register.get_handler(field_obj)
                if handler:
                    value = handler.generate()
                    setattr(instance, field_name, value)

