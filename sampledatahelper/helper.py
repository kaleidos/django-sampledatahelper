#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from django.conf import settings
from .mixins import NumberMixin, TextMixin, TimeMixin, LocalizedMixin, ImageMixin, OtherMixin


class SampleDataHelper(NumberMixin, TextMixin, TimeMixin, LocalizedMixin, ImageMixin, OtherMixin):
    def __init__(self, seed=None):
        if seed is None:
            seed = getattr(settings, 'SAMPLEDATAHELPER_SEED', None)

        if seed is not None:
            random.seed(seed)
