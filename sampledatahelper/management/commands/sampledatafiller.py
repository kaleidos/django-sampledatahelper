from django.core.management.base import BaseCommand
from django.conf import settings

from sampledatahelper.compat import get_model
from sampledatahelper.model_helper import ModelDataHelper

class Command(BaseCommand):
    args = ''
    help = 'Example data generator'
    mdh = ModelDataHelper(seed=12345678901)

    def handle(self, *args, **options):
        for model_conf in settings.SAMPLEDATAHELPER_MODELS:
            app_label, model_name = model_conf.get('model').split(".")
            instances_number = model_conf.get('number')
            fields_overwrite = model_conf.get('fields_overwrite', {})
            model = get_model(app_label, model_name)
            self.mdh.fill_model(model, instances_number, *fields_overwrite)
