Model Data Helper
=================

Model data helper easy the models population introspecting in the django model
fields.

.. py:class:: ModelDataHelper(seed=None)

    Initialize the seed of the instance of model data helper, to allwais
    generate the same data.

.. py:method:: ModelDataHelper.fill_model(model, number, \*args, \*\*kwargs)

    Generate a number of instances of the model and save it. You can overwrite
    the default data generator adding extra kwargs arguments.

    To overwrite a field generation behavior you have to add extra arguments.
    with the name of the field, and the value must be, a fixed value or a
    callable object that receive 2 parameters, the model instance, and a
    SampleDataHelper instance. This overwrite is done alwais at the end of
    fill_model, this mean you can access all auto-generated data in other
    instance fields. This extra arguments can be a named argument using the
    field name as argument name, and the callable as value, or a not named name
    with value a tuple of field name and the callable. Examples::

      fill_model(ModelName, 10, ('field_name', lambda instance, sd: sd.int()))
      fill_model(ModelName, 10, field_name=lambda instance, sd: sd.int())

    The order of field generation is, first the not overwrited fields in any
    order, second the overwrited fields in args, in the same order the
    parameters, and third the overwrited fields in kwargs in any orders. If you
    want to asure the ordering, use the args overwrite.

.. py:method:: ModelDataHelper.fill_model_instance(instance, \*args, \*\*kwargs)

    Fill a instance of a django model. You can overwrite the default data
    generator adding extra arguments like in `fill_model` method. Examples::

      fill_model_instance(instance, ('field_name', lambda instance, sd: sd.int()))
      fill_model_instance(instance, field_name=lambda instance, sd: sd.int())
