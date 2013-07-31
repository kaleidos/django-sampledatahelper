import os
import random
from django.core.files.images import ImageFile
try:
    from sampledatahelper.image_generators import ImgSimple, ImgPlasma, ImgMandelbrot, ImgIFS
    PIL_INSTALLED = True
except ImportError:
    PIL_INSTALLED = False
from tempfile import mkstemp

from sampledatahelper.exceptions import ParameterError, NotChoicesFound


class ImageMixin(object):
    def image_from_directory(self, directory_path, valid_extensions=['.jpg', '.bmp', '.png']):
        if not os.path.exists(directory_path):
            raise ParameterError('directory_path must be a valid path')

        list_of_images = os.listdir(directory_path)
        list_of_images = list(filter(lambda x: os.path.splitext(x)[1] in valid_extensions, list_of_images))

        if len(list_of_images) == 0:
            raise NotChoicesFound('Not valid images found in directory_path for valid_extensions')

        random_path = os.path.join(directory_path, random.choice(list_of_images))
        im_file = ImageFile(open(random_path, 'r'))
        return im_file

    def image(self, width, height, typ="simple"):
        if not PIL_INSTALLED:
            raise ImportError("PIL needed to use this function")

        if width <= 0 or height <= 0:
            raise ParameterError('width and width must be geater than 0')

        if typ == "simple":
            generator = ImgSimple()
        elif typ == "plasma":
            generator = ImgPlasma()
        elif typ == "mandelbrot":
            generator = ImgMandelbrot()
        elif typ == "ifs":
            generator = ImgIFS()
        elif typ == "random":
            generator = self.choice([ImgSimple, ImgPlasma, ImgMandelbrot, ImgIFS])()
        else:
            raise ParameterError('Unknown image generator type')

        im = generator.generate(self, width, height)

        tf, tfname = mkstemp(suffix=".png")

        im.save(tfname)

        im_file = ImageFile(open(tfname, 'rb'))

        return im_file
