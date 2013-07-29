#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from django.conf import settings
from django.db import models
from django.db.models.fields import FieldDoesNotExist

from .mixins import NumberMixin, TextMixin, TimeMixin, LocalizedMixin, ImageMixin, OtherMixin
from .exceptions import ParameterError


class SampleDataHelper(NumberMixin, TextMixin, TimeMixin, LocalizedMixin, ImageMixin, OtherMixin):
    def __init__(self, seed=None):
        if seed is None:
            seed = getattr(settings, 'SAMPLEDATAHELPER_SEED', None)

        if seed is not None:
            random.seed(seed)

class ModelDataHelper(object):
    def __init__(self, seed=None):
        self.sd = SampleDataHelper(seed)

    def __get_model_fields():
        return model._meta.fields

    def fill_model_instance_field(self, instance, field):
        pass

    def fill_model(self, model, number, **kwargs):
        if number <= 0:
            raise ParameterError('number must be greater than 0')

        if not issubclass(model, models.Model):
            raise ParameterError('model must be a django model subclass')

        for x in range(number):
            instance = model()
            self.fill_model_instance(instance, **kwargs)
            instance.save()

    def __get_instance_fields(self, instance):
        fields = []
        for field_name in instance._meta.get_all_field_names():
            try:
                fields.append((field_name, instance._meta.get_field(field_name)))
            except FieldDoesNotExist:
                pass
        return fields

    def fill_model_instance(self, instance, **kwargs):
        if not isinstance(instance, models.Model):
            raise ParameterError('instance must be a django model instance')

        for field in self.__get_instance_fields(instance):
            if field in kwargs:
                if isinstance(kwargs[field], dict) and 'method' in kwargs[field]:
                    setattr(
                        instance,
                        field,
                        kwargs[field]['method'](
                            self.sd,
                            *kwargs[field]['args'],
                            **kwargs[field]['kwargs']
                        )
                    )
                else:
                    setattr(
                        instance,
                        field,
                        kwargs[field]['method'],
                    )
            else:
                self.fill_model_instance_field(instance, field)
