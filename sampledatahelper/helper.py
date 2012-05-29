#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
try:
    from django.contrib.webdesign import lorem_ipsum
except ImportError:
    sys.exit()

import datetime as dt
import random
import Image
import ImageDraw, ImageFont
from django.utils.timezone import utc
from tempfile import mkstemp
from django.core.files.images import ImageFile
from .image_generators import *
from .name_generators import *

class SampleDataHelper(object):
    def __init__(self, seed = None):
        if seed != None:
            random.seed(seed)
        self.app_directory = os.path.dirname(os.path.abspath(__file__))
        self.tags_list = []
        self.ttf_font = ImageFont.truetype(self.app_directory+"/static/font.ttf", 80)

        self.images_cache = {}
    
    def word(self):
        """Random text with 1 word."""
        return lorem_ipsum.words(1, common=False)
        
    def words(self, min_words=1, max_words=5):
        """Random text with 1 word."""
        words = random.randint(min_words, max_words)
        return lorem_ipsum.words(words, common=False)
        
    def email(self):
        """Random mail address."""
        return lorem_ipsum.words(1, common=False) + u'@' + lorem_ipsum.words(1, common=False) + \
               random.choice([u'.es', u'.com', u'.org', u'.net', u'.gov', u'.tk'])
    
    def int(self, *args, **kwargs):
        """Random number from 0 or min_value to max_value - 1 or sys.maxint - 1."""
        if len(kwargs.keys()) > 0:
            min_value = 0
            max_value = sys.maxint
            if 'min_value' in kwargs.keys():
                min_value = kwargs['min_value']
            if 'max_value' in kwargs.keys():
                max_value = kwargs['max_value']
        else:
            if len(args) == 0:
                min_value = 0
                max_value = sys.maxint
            elif len(args) == 1:
                min_value = 0
                max_value = args[0]
            else: 
                min_value = args[0]
                max_value = args[1]
        return random.randrange(min_value, max_value)
    
    def province_code(self):
        """Random province code."""
        return random.choice(
            ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
             '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
             '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
             '51', '52', 'AD', ]
        )
    
    def sentence(self):
        """Random text with variable number of words, one sentence."""
        return lorem_ipsum.sentence()[:255]
    
    def paragraph(self):
        """Random text with variable number of words, several sentences."""
        return lorem_ipsum.paragraph()    
    
    def number(self, ndigits):
        """Random number from 0 to 999[with the given number of digits]."""
        return random.randrange(0, 10 ** ndigits)
    
    def float(self, min, max):
        """Random float from min to max"""
        return (max - (random.random() * (max - min)))
    
    def number_string(self, ndigits):
        """Random number from 0 to ndigits, in string format, filled by 0s on the left."""
        return u''.join(random.choice(u'0123456789') for i in range(ndigits))
    
    def name(self, locale=None, number=1, as_dict=False):
        return Name().generate(self, locale, number, as_dict)

    def surname(self, locale=None, number=1, as_dict=False):
        return Surname().generate(self, locale, number, as_dict)

    def fullname(self, locale=None, as_dict=False):
        return FullName().generate(self, locale, as_dict)

    def slug(self, min_words=5, max_words=5):
        """Random slug"""
        return "-".join([ self.word() for x in range(self.int(max_value=max_words, min_value=min_words))])
    
    def boolean(self):
        return random.randrange(0, 2) == 0
    
    def choice(self, choices):
        return random.choice(choices)
    
    def image(self, width, height, typ="simple"):
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
    
    def future_date(self, min_distance=0, max_distance=365):
        """Random date between today and today + one year - one day."""
        return dt.date.today() + dt.timedelta(random.randrange(min_distance, max_distance))
    
    def past_date(self, min_distance=0, max_distance=365):
        """Random date between today and today + one year - one day."""
        return dt.date.today() - dt.timedelta(random.randrange(min_distance, max_distance))

    def future_datetime(self, min_distance=0, max_distance=1440):
        """Random date between today and today + one year - one day."""
        return dt.datetime.utcnow().replace(tzinfo=utc) + dt.timedelta(minutes=random.randrange(min_distance, max_distance))
    
    def past_datetime(self, min_distance=0, max_distance=1440):
        """Random date between today and today + one year - one day."""
        return dt.datetime.utcnow().replace(tzinfo=utc) - dt.timedelta(minutes=random.randrange(min_distance, max_distance))

    def date(self, begin=-365, end=365):
        """Random date between today - one year and today + one year."""
        return dt.date.today() - dt.timedelta(random.randrange(begin, end))

    def datetime(self, begin=-1440, end=1440):
        """Random date between today - one year and today + one year."""
        return dt.datetime.utcnow().replace(tzinfo=utc) - dt.timedelta(minutes=random.randrange(begin, end))

    def tags(self, max_tags):
        tags = []
        for i in range(random.randrange(0, max_tags)):
            tags.append(self.tags_list[random.randrange(0, len(self.tags_list))])
        return ','.join(tags)

    def db_object(self, model):
        count = model.objects.all().count()
        return model.objects.all()[self.int(max_value=count)]
    
    def db_object_from_queryset(self, queryset):
        count = queryset.all().count()
        return queryset.all()[self.int(max_value=count)]

