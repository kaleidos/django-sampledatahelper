import random
import os
import io

from django.core.files.base import ContentFile

from ..exceptions import ParameterError, NotChoicesFound


class OtherMixin(object):
    def boolean(self):
        return random.randrange(0, 2) == 0

    def nullboolean(self):
        return random.choice([None, True, False])

    def choice(self, choices):
        if not isinstance(choices, list) and not isinstance(choices, tuple):
            raise ParameterError('choices must be a list or a tuple')

        if choices == []:
            raise ParameterError('choices can\'t be a empty list')

        return random.choice(choices)

    def choices_key(self, choices):
        if not isinstance(choices, list) and not isinstance(choices, tuple):
            raise ParameterError('choices must be a list or a tuple')

        try:
            return self.choice(choices)[0]
        except (TypeError, ValueError, ParameterError):
            raise ParameterError('choices must be a valid django choices list')

    def db_object(self, model, raise_not_choices=True):
        if model.objects.all().count() > 0:
            return self.db_object_from_queryset(model.objects.all())

        if raise_not_choices:
            raise NotChoicesFound('Emtpy queryset')

        return None

    def db_object_from_queryset(self, queryset, raise_not_choices=True):
        count = queryset.all().count()
        if count > 0:
            return queryset.all()[self.int(max_value=count-1)]

        if raise_not_choices:
            raise NotChoicesFound('Emtpy queryset')

        return None

    def ipv4(self):
        return "{0}.{1}.{2}.{3}".format(
            self.int(0, 255),
            self.int(0, 255),
            self.int(0, 255),
            self.int(0, 255),
        )

    def ipv6(self):
        return "{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}".format(
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4),
            self.hex_chars(1, 4)
        )

    def mac_address(self):
        return "{0}:{1}:{2}:{3}:{4}:{5}".format(
            self.hex_chars(2, 2),
            self.hex_chars(2, 2),
            self.hex_chars(2, 2),
            self.hex_chars(2, 2),
            self.hex_chars(2, 2),
            self.hex_chars(2, 2),
        )

    def hex_chars(self, min_chars=1, max_chars=5):

        if min_chars > max_chars:
            raise ParameterError('min_chars greater than max_chars')

        result = ""
        chars = random.randint(min_chars, max_chars)
        for x in range(chars):
            result += self.choice(['0', '1', '2', '3', '4', '5', '6', '7',
                                   '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'])
        return result

    def path(self, absolute=None, extension='', min_levels=1, max_levels=5):
        if min_levels > max_levels:
            raise ParameterError('min_levels greater than max_levels')

        if absolute is None:
            absolute = self.boolean()

        if absolute:
            result = "/"
        else:
            result = ""

        levels = random.randint(min_levels, max_levels)
        for x in range(levels):
            result += self.word()
            if x != max_levels - 1:
                result += "/"

        result += extension

        return result

    def file_from_directory(self, directory_path, valid_extensions=['.jpg', '.bmp', '.png']):
        if not os.path.exists(directory_path):
            raise ParameterError('directory_path must be a valid path')

        list_of_images = os.listdir(directory_path)
        list_of_images = list(filter(lambda x: os.path.splitext(x)[1] in valid_extensions, list_of_images))

        if len(list_of_images) == 0:
            raise NotChoicesFound('Not valid images found in directory_path for valid_extensions')

        random_path = os.path.join(directory_path, random.choice(list_of_images))

        fd = open(random_path, 'rb')
        file_data = ContentFile(fd.read(), name=os.path.basename(random_path))
        fd.close()
        return file_data
