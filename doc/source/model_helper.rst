Model Data Helper
=================

Model data helper easy the models population introspecting in the django model
fields.

.. class:: ModelDataHelper(seed=None)

    Initialize the seed of the instance of model data helper, to allwais
    generate the same data.

.. method:: ModelDataHelper.fill_model(model, number, \*\*kwargs)

    Generate a number of instances of the model and save it. You can overwrite
    the default data generator adding extra kwargs arguments.

    To overwrite a field generation behavior you have to add a extra argument
    with the name of the field, and the value must be, a fixed value or a
    callable object that receive 2 parameters, the model instance, and a
    SampleDataHelper instance.

.. method:: ModelDataHelper.fill_model_instance(instance, \*\*kwargs)

    Fill a instance of a django model. You can overwrite the default data
    generator adding extra kwargs arguments like in `fill_model` method.
