Quick start
===========

Follow the install and configure instructions.

If you have some aplications to populate, you can split your sample data
generation on one command per app, or add only one command in one app thats
generate everything. Anyway you have to build a command files.

The file must be in `<app-module>/management/commands/<command-name>.py` can be
something like `myapp/management/commands/mysampledata.py`.

And finally the command file content can be like this::

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

To generate your sampledata, simply run the created command, for example::

  python manage.py mysampledata
