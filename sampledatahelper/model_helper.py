from django.db import models
from django.db.models.fields import FieldDoesNotExist

import django
from distutils.version import StrictVersion

from sampledata.exceptions import ParameterError

from .helper import SampleDataHelper
from .register import register

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('sampledatahelper')


class ModelDataHelper(object):
    def __init__(self, seed=None):
        self.sd = SampleDataHelper(seed)

    def __get_instance_fields(self, instance):
        django_version = django.get_version()
        if StrictVersion(django_version) >= StrictVersion('1.8'):
            return self.__get_instance_fields_django_18(instance)
        return self.__get_instance_fields_django_other(instance)

    def __get_instance_fields_django_other(self, instance):
        fields = []
        for field_name in instance._meta.get_all_field_names():
            try:
                fields.append((field_name, instance._meta.get_field(field_name)))
            except FieldDoesNotExist:
                pass
        return fields

    def __get_instance_fields_django_18(self, instance):
        fields = []
        for field in instance._meta.get_fields():
            try:
                fields.append((field.name, field))
            except FieldDoesNotExist:
                pass
        return fields

    def fill_model(self, model, number, *args, **kwargs):
        if number <= 0:
            raise ParameterError('number must be greater than 0')

        if not issubclass(model, models.Model):
            raise ParameterError('model must be a django model subclass')

        logger.debug("Filling model %s.%s with %d instances" % (model._meta.app_label, model.__name__, number))

        for x in range(number):
            instance = model()
            logger.debug("Filling instance %d" % (x))
            self.fill_model_instance(instance, *args, **kwargs)
            instance.save()

    def fill_model_instance(self, instance, *args, **kwargs):
        if not isinstance(instance, models.Model):
            raise ParameterError('instance must be a django model instance')

        for field_name, field_obj in self.__get_instance_fields(instance):
            if field_name not in kwargs:
                handler = register.get_handler(field_obj)
                if handler:
                    value = handler.generate()
                    setattr(instance, field_name, value)

        for field in args:
            if hasattr(field[1], '__call__'):
                value = field[1](instance, self.sd)
            else:
                value = field[1]
            setattr(instance, field[0], value)

        for field_name in kwargs.keys():
            if hasattr(kwargs[field_name], '__call__'):
                value = kwargs[field_name](instance, self.sd)
            else:
                value = kwargs[field_name]
            setattr(instance, field_name, value)
