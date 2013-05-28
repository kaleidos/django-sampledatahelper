Django Sample Data Helper
=========================

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
      sd = None
  
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

SampleDataHelper Methods
------------------------

Available methods:

+----------------------------------------------------+--------------------------------------+
| Method                                             | return                               |
+====================================================+======================================+
| word()                                             | a word                               |
+----------------------------------------------------+--------------------------------------+
| words(min_words=1, max_words=5)                    | a string with n words                |
+----------------------------------------------------+--------------------------------------+
| email()                                            | an email                             |
+----------------------------------------------------+--------------------------------------+
| int(max_value=sys.maxint, min_value=0)             | an integer between min and max value |
+----------------------------------------------------+--------------------------------------+
| state_code(locale)                                 | a state code for the locale country  |
+----------------------------------------------------+--------------------------------------+
| sentence()                                         | a sentence (max 255 caracters)       |
+----------------------------------------------------+--------------------------------------+
| short_sentence()                                   | a sentence (max 100 caracters)       |
+----------------------------------------------------+--------------------------------------+
| long_sentence()                                    | a sentence (min 150 caracters)       |
+----------------------------------------------------+--------------------------------------+
| paragraph()                                        | a paragraph                          |
+----------------------------------------------------+--------------------------------------+
| number(ndigits)                                    | a number of n digits as max          |
+----------------------------------------------------+--------------------------------------+
| digits(ndigits)                                    | a number of exactly n digits         |
+----------------------------------------------------+--------------------------------------+
| float(self, min, max)                              | a float from min to max              |
+----------------------------------------------------+--------------------------------------+
| number_string(self, ndigits)                       | a string of n digits                 |
+----------------------------------------------------+--------------------------------------+
| name(locale=None, number=1, as_list=False)         | a string or list of tipical names    |
|                                                    | from locale using n names (compound  |
|                                                    | names)                               |
+----------------------------------------------------+--------------------------------------+
| surname(locale=None, number=1, as_list=False)      | a string or list of tipical surnames |
|                                                    | from locale using n surnames         |
+----------------------------------------------------+--------------------------------------+
| fullname(locale=None, as_list=False)               | a string or list of tipical          |
|                                                    | names+surnames from locale           |
+----------------------------------------------------+--------------------------------------+
| slug(min_words=5, max_words=5)                     | a slug between min_words and         |
|                                                    | max_words words                      |
+----------------------------------------------------+--------------------------------------+
| boolean()                                          | a boolean value                      |
+----------------------------------------------------+--------------------------------------+
| choice(choices)                                    | a value from a list                  |
+----------------------------------------------------+--------------------------------------+
| image(width, height, typ="simple")                 | an image of WIDTHxHEIGHT size        |
|                                                    | generated with the typ generator     |
+----------------------------------------------------+--------------------------------------+
| image_from_directory(directory_path,               | an image from a directory with a     |
| valid_extensions=['.jpg', '.bmp', '.png'])         | valid extension                      |
+----------------------------------------------------+--------------------------------------+
| date_between(min_date, max_date)                   | a date between the min_date and      |
|                                                    | max_date date objects                |
+----------------------------------------------------+--------------------------------------+
| future_date(min_distance=0, max_distance=365)      | a future date between                |
|                                                    | now+min_distance and                 |
|                                                    | now+max_distance in days             |
+----------------------------------------------------+--------------------------------------+
| past_date(min_distance=0, max_distance=365)        | a past date between                  |
|                                                    | now-max_distance and                 |
|                                                    | now-min_distance in days             |
+----------------------------------------------------+--------------------------------------+
| datetime_between(min_datetime, max_datetime)       | a datetime between the min_datetime  |
|                                                    | and max_datetime datetime objects    |
+----------------------------------------------------+--------------------------------------+
| future_datetime(min_distance=0, max_distance=1440) | a future datetime between            |
|                                                    | now+min_distance and                 |
|                                                    | now+max_distance in minutes          |
+----------------------------------------------------+--------------------------------------+
| past_datetime(min_distance=0, max_distance=1440)   | a past datetime between              |
|                                                    | now-max_distance and                 |
|                                                    | now-min_distance in minutes          |
+----------------------------------------------------+--------------------------------------+
| date(begin=-365, end=365)                          | a date between now+begin and now+end |
|                                                    | in days                              |
+----------------------------------------------------+--------------------------------------+
| datetime(begin=-1440, end=1440)                    | a datetime between now+begin and     |
|                                                    | now+end in minutes                   |
+----------------------------------------------------+--------------------------------------+
| tags(max_tags)                                     | a string with some tags separated    |
|                                                    | by commas                            |
+----------------------------------------------------+--------------------------------------+
| db_object(model)                                   | a random object from the model       |
+----------------------------------------------------+--------------------------------------+
| db_object_from_queryset(queryset)                  | a random object from the queryset    |
+----------------------------------------------------+--------------------------------------+
| phone(locale, country_code)                        | a phone number from a country with   |
|                                                    | or without country code              |
+----------------------------------------------------+--------------------------------------+
| zip_code(locale)                                   | a zip code for a country             |
+----------------------------------------------------+--------------------------------------+
| id_card(locale)                                    | a identification card code for a     |
|                                                    | country                              |
+----------------------------------------------------+--------------------------------------+
