Django Sample Data Helper
=========================

.. image:: http://kaleidos.net/static/img/badge.png
    :target: http://www.kaleidos.net/community/django-tint/

.. image:: https://travis-ci.org/kaleidos/django-sampledatahelper.png?branch=master
    :target: https://travis-ci.org/kaleidos/django-sampledatahelper

.. image:: https://coveralls.io/repos/kaleidos/django-sampledatahelper/badge.png?branch=master
    :target: https://coveralls.io/r/kaleidos/django-sampledatahelper?branch=master

.. image:: https://pypip.in/v/django-sampledatahelper/badge.png
    :target: https://crate.io/packages/django-sampledatahelper

.. image:: https://pypip.in/d/django-sampledatahelper/badge.png
    :target: https://crate.io/packages/django-sampledatahelper

Helper class to create django sample data.

Example
-------

Sample data command for generate instances of MyModel::

  from django.core.management.base import BaseCommand
  from myapp.models import MyModel
  from sampledatahelper.helper import SampleDataHelper
  
  class Command(BaseCommand):
      args = ''
      help = 'Example data generator'
      sd = SampleDataHelper(seed=12345678901)
  
      def generate_mymodel_data(self, instances):
          for x in range(instances):
              instance = MyModel.objects.create(
                  slug=self.sd.slug(2, 3),
                  name=self.sd.name(2, 3)
                  claim=self.sd.sentence(),
                  description=self.sd.paragraph(),
                  email=self.sd.email(),
                  photo=self.sd.image(64, 64),
                  is_active=self.sd.boolean(),
                  birth_date=self.sd.past_date(),
                  expected_death_date=self.sd.future_date(),
                  my_related_object=self.sd.db_object(MyRelatedModel)
              )

      def handle(self, *args, **options):
          print "Generating MyModel data"
          self.generate_mymodel_data(5)

Documentation
-------------

Read the Docs: https://django-sample-data-helper.readthedocs.org/en/latest/
