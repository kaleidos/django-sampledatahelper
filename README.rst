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

  from django.core.management.base import BaseCommand, CommandError
  from myapp.models import MyModel
  from sampledatahelper.helper import SampleDataHelper
  
  class Command(BaseCommand):
      args = ''
      help = 'Example data generator'
  
      def handle(self, *args, **options):
          sd = SampleDataHelper(seed=12345678901)
  
          INSTANCES = 5
  
          for x in range(INSTANCES):
              instance = MyModel.objects.create(
                      slug=sd.slug(2, 3),
                      name=sd.name(2, 3)
                      claim=sd.sentence(),
                      description=sd.paragraph(),
                      email=sd.email(),
                      photo=sd.image(64, 64),
                      is_active=sd.boolean(),
                      birth_date=sd.past_date(),
                      expected_death_date=sd.future_date(),
                      my_related_object=sd.db_object(MyRelatedModel)
              )

Documentation
-------------

Read the Docs: https://django-sample-data-helper.readthedocs.org/en/latest/
