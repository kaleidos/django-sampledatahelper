Django Sample Data Helper
=========================

Helper class to create django sample data.

Example
-------

Sample data command for generate instances of MyModel::

  from django.core.management.base import BaseCommand, CommandError
  from myapp.models import MyModel
  from sampledatahelper import SampleDataHelper
  
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

Available methods::

    word(): return a word
    email(): return an email
    int(max_value, min_value): return an integer (default min_value = 0)
    province_code(): Return an spain province code
    sentence(): Return an sentence (max 255 caracters)
    paragraph(): Return a paragraph.
    number(ndigits): Return a number of n digits
    float(self, min, max): Return a float from min to max
    number_string(self, ndigits): Return a numer of n digits in string format
    name(min_words, max_words): Return a name between min_words and max_words words (default min_words = 5, default max_words = 5)
    slug(min_words, max_words): Return a slug between min_words and max_words words (default min_words = 5, default max_words = 5)
    boolean(): Returns a boolean value
    image(width, height): Return an image of WIDTHxHEIGHT size
    future_date(min_distance=0, max_distance=365): A future date between now+min_distance and now+max_distance in days (default begin = 0, default end = 365)
    past_date(min_distance=0, max_distance=365): A past date between now+max_distance and now+min_distance in days (default begin = 0, default end = 365)
    future_datetime(min_distance=0, max_distance=1440): A future datetime between now+min_distance and now+max_distance in minutes (default begin = 0, default end = 1440)
    past_datetime(min_distance=0, max_distance=1440): A past datetime between now+max_distance and now+min_distance in minutes (default begin = 0, default end = 1440)
    date(begin=-365, end=365): A date between now+begin and now+end in days (default begin = -365, default end = 365)
    datetime(begin=-1440, end=1440): A datetime between now+begin and now+end in minutes (default begin = -1440, default end = 1440)
    tags(max_tags): Return a string with some tags separated by commas
    db_object(model): Return an random object from the database
