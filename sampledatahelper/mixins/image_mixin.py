import os
import random
from django.core.files.images import ImageFile
try:
    from .image_generators import ImgSimple, ImgPlasma, ImgMandelbrot, ImgIFS
    PIL_INSTALLED = True
except ImportError:
    PIL_INSTALLED = False
from tempfile import mkstemp


class ImageMixin(object):
    def image_from_directory(self, directory_path, valid_extensions=['.jpg', '.bmp', '.png']):
        list_of_images = os.listdir(directory_path)
        list_of_images = filter(lambda x: os.path.splitext(x)[1] in valid_extensions, list_of_images)
        random_path = os.path.join(directory_path, random.choice(list_of_images))
        im_file = ImageFile(open(random_path, 'r'))
        return im_file

    def image(self, width, height, typ="simple"):
        if not PIL_INSTALLED:
            raise Exception("PIL needed to use this function")

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
            generator = ImgSimple()

        im = generator.generate(self, width, height)

        tf, tfname = mkstemp(suffix=".png")

        im.save(tfname)

        im_file = ImageFile(open(tfname, 'r'))

        return im_file
