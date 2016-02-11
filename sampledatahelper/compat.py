# -*- coding: utf-8 -*-


# get model
get_model = None
try:
    # django < 1.9
    from django.db.models import loading
    get_model = loading.get_model
except ImportError:
    # django >= 1.9
    from django.apps import apps
    get_model = apps.get_model

