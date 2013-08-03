Install and configure
=====================

Install using pip, including any pillow if you want image genetion...::

  pip install django-sampledatahelper
  pip install pillow  # For image generation

You can configure, if you want a ``SAMPLEDATAHELPER_SEED`` variable in your
settings, to generate alwais the same data. Example::

  SAMPLEDATAHELPER_SEED = 123456789

If you want to use the ``sampledatafiller`` command, you have to define
your ``SAMPLEDATAHELPER_MODELS`` with the list of models you want to fill. Example::

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
