Django Sample Data Helper
=========================

.. image:: http://kaleidos.net/static/img/badge.png
    :target: http://www.kaleidos.net/community/django-sampledatahelper/

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

Sample data command for generate instances of MyModel

.. code:: python

  from django.core.management.base import BaseCommand
  from django.contrib.auth.models import User
  from sampledatahelper.model_helper import ModelDataHelper
  from sampledatahelper.helper import SampleDataHelper
  
  class Command(BaseCommand):
      args = ''
      help = 'Example data generator'
      mdh = ModelDataHelper(seed=12345678901)
  
      def handle(self, *args, **options):
          print "Generating MyModel data"
          # Generate 5 instances completly random
          self.mdh.fill_model(MyModel, 5)
  
          # Generate 5 instances selecting random method for some fields
          self.mdh.fill_model(MyModel,
                              5,
                              my_int_field={'method': SampleDataHelper.int, 'args': [5, 10]})
  
          # Generate 5 instances with fixed data in a field
          self.mdh.fill_model(MyModel,
                              5,
                              my_int_field=8)

Documentation
-------------

Read the Docs: https://django-sample-data-helper.readthedocs.org/en/latest/
