Django Sample Data Helper
=========================

.. image:: http://kaleidos.net/static/img/badge.png
    :target: http://www.kaleidos.net/community/django-sampledatahelper/

.. image:: https://img.shields.io/travis/kaleidos/django-sampledatahelper/master.svg
    :target: https://travis-ci.org/kaleidos/django-sampledatahelper

.. image:: https://img.shields.io/coveralls/kaleidos/django-sampledatahelper.svg
    :target: https://coveralls.io/r/kaleidos/django-sampledatahelper?branch=master

.. image:: https://img.shields.io/pypi/v/django-sampledatahelper.svg
    :target: https://pypi.python.org/pypi/django-sampledatahelper

App to automatically populate django database.

Install and configure
=====================

You need at least django >= 1.7.

Install using pip, including any pillow if you want image genetion...:

.. code:: bash

  pip install django-sampledatahelper
  pip install pillow  # For image generation

You can configure, if you want a :code:`SAMPLEDATAHELPER_SEED` variable in your
settings, to generate alwais the same data. Example:

.. code:: python

  SAMPLEDATAHELPER_SEED = 123456789

If you want to use the :code:`sampledatafiller` command, you have to define
your :code:`SAMPLEDATAHELPER_MODELS` with the list of models you want to fill. Example:

.. code:: python

  SAMPLEDATAHELPER_MODELS = [
      # Generate 5 instances completly random
      { 'model': 'myapp.MyModel', 'number': 5, },
  
      # Generate 5 instances selecting random method for some fields
      {
          'model': 'myapp.MyModel',
          'number': 5,
          'fields_overwrite': [
              ('my_int_field', lambda _, sd: sd.int(5, 10)),
          ]
      },
  
      # Generate 5 instances with fixed data in a field
      {
          'model': 'myapp.MyModel',
          'number': 5,
          'fields_overwrite': [
              ('my_int_field', 5),
          ]
      }
  ]

Quick start
===========

Follow the install and configure instructions.

With Django sampledatahelper you have 2 options to populate your database

Using SampleDataFiller
----------------------

Sample data filler is a command that use the :code:`SAMPLEDATAHELPER_MODELS` setting
variable to populate your database. Example:

.. code:: python

  SAMPLEDATAHELPER_MODELS = [
      # Generate 5 instances completly random
      { 'model': 'myapp.MyModel', 'number': 5, },

      # Generate 5 instances selecting random method for some fields
      {
          'model': 'myapp.MyModel',
          'number': 5,
          'fields_overwrite': [
              ('my_int_field', lambda _, sd: sd.int(5, 10)),
          ]
      },

      # Generate 5 instances with fixed data in a field
      {
          'model': 'myapp.MyModel',
          'number': 5,
          'fields_overwrite': [
              ('my_int_field', 5),
          ]
      }
  ]

Then you only have to run::

  python manage.py sampledatafiller

Using a custom sampledata command
---------------------------------

You can create a command to fill your models manullay to take more control.

If you have some applications to populate, you can split your sample data
generation on one command per app, or add only one command in one app thats
generate everything.

The file must be in :code:`<app-module>/management/commands/<command-name>.py` can be
something like :code:`myapp/management/commands/mysampledata.py`.

The easy way to build your command is using :code:`ModelDataHelper`.

.. code:: python

  from django.core.management.base import BaseCommand
  from myapp.models import MyModel
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
                              my_int_field=lambda instance, sd: sd.int(5, 10))
  
          # Generate 5 instances with fixed data in a field
          self.mdh.fill_model(MyModel, 5, my_int_field=8)

You can build a more precise command using directly the :code:`SampleDataHelper`.

.. code:: python

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
                  name=self.sd.name(2, 3),
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

To generate your sampledata, simply run the created command, for example::

  python manage.py mysampledata



Documentation
-------------

Read the Docs: https://django-sample-data-helper.readthedocs.org/en/latest/
