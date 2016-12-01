#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import io
import os

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

from sampledata.helper import SampleData
from sampledata.exceptions import NotChoicesFound, ParameterError

from sampledatahelper.compat import get_model

class SampleDataHelper(SampleData):
    def __init__(self, seed=None):
        if seed is None:
            seed = getattr(settings, 'SAMPLEDATAHELPER_SEED', None)

        if seed is not None:
            random.seed(seed)

    def choices_key(self, choices):
        if not isinstance(choices, list) and not isinstance(choices, tuple):
            raise ParameterError('choices must be a list or a tuple')

        try:
            return self.choice(choices)[0]
        except (TypeError, ValueError, ParameterError):
            raise ParameterError('choices must be a valid django choices list')

    def db_object(self, model, raise_not_choices=True):
        if isinstance(model, str):
            model = get_model(model)
        if model.objects.all().count() > 0:
            return self.db_object_from_queryset(model.objects.all())

        if raise_not_choices:
            raise NotChoicesFound('Emtpy queryset')

        return None

    def db_object_from_queryset(self, queryset, raise_not_choices=True):
        count = queryset.all().count()
        if count > 0:
            return queryset.all()[self.int(max_value=count-1)]

        if raise_not_choices:
            raise NotChoicesFound('Emtpy queryset')

        return None

    def image_from_directory(self, directory_path, valid_extensions=['.jpg', '.bmp', '.png']):
        random_path = self.image_path_from_directory(directory_path, valid_extensions)

        fd = open(random_path, 'rb')
        stream = io.BytesIO(fd.read())
        fd.close()
        im_file = ImageFile(file=stream, name=os.path.basename(random_path))
        return im_file

    def image(self, width, height, typ="simple"):
        stream = self.image_stream(width, height, typ)
        im_file = ImageFile(file=stream, name="random_image.png")
        return im_file

    def file_from_directory(self, directory_path, valid_extensions=['.jpg', '.bmp', '.png']):
        random_path = self.path_from_directory(directory_path, valid_extensions)

        fd = open(random_path, 'rb')
        file_data = ContentFile(fd.read(), name=os.path.basename(random_path))
        fd.close()
        return file_data
