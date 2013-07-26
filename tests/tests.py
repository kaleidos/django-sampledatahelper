from django.utils import unittest
from django.core.validators import validate_email, validate_slug, URLValidator

import string
import datetime

from sampledatahelper.helper import SampleDataHelper
from sampledatahelper.exceptions import ParameterError


class TestNumberHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

    def test_int(self):
        self.assertEqual(self.sd.int(min_value=5, max_value=5), 5)

        self.assertTrue(self.sd.int(min_value=1000000000) >= 1000000000)
        self.assertTrue(self.sd.int(max_value=3) <= 3)

        self.assertTrue(isinstance(self.sd.int(), int))

        val = self.sd.int(5, 10)
        self.assertTrue(val <= 10)
        self.assertTrue(val >= 5)

        with self.assertRaises(ParameterError):
            self.sd.int(10, 5)

    def test_number(self):
        self.assertTrue(len(str(self.sd.number(5))) <= 5)

        with self.assertRaises(ParameterError):
            self.sd.number(0)

        with self.assertRaises(ParameterError):
            self.sd.number(-1)

    def test_digits(self):
        self.assertEqual(len(str(self.sd.digits(5))), 5)

        with self.assertRaises(ParameterError):
            self.sd.digits(0)

        with self.assertRaises(ParameterError):
            self.sd.digits(-1)

    def test_float(self):
        value = self.sd.float(1, 5)
        self.assertTrue(isinstance(value, float))
        self.assertTrue(value >= 1)
        self.assertTrue(value <= 5)

        self.assertEqual(self.sd.float(0, 0), 0)
        self.assertEqual(self.sd.float(5, 5), 5)
        self.assertEqual(self.sd.float(-5, -5), -5)

        with self.assertRaises(ParameterError):
            self.sd.float(10, 5)

    def test_number_string(self):
        value = self.sd.number_string(5)
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value), 5)

        self.assertEqual(self.sd.number_string(0), '')

        with self.assertRaises(ParameterError):
            self.sd.number_string(-1)


class TestTextHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

    def test_char(self):
        value = self.sd.char()
        self.assertTrue(isinstance(value, basestring))
        self.assertTrue(value in string.letters)

    def test_chars(self):
        value = self.sd.chars()
        self.assertTrue(isinstance(value, basestring))
        self.assertTrue(len(value) >= 1)
        self.assertTrue(len(value) <= 5)

        value = self.sd.chars(5, 5)
        self.assertTrue(len(value) == 5)

        self.assertEqual(self.sd.chars(0, 0), '')

        with self.assertRaises(ParameterError):
            value = self.sd.chars(10, 5)

    def test_word(self):
        value = self.sd.word()
        self.assertTrue(isinstance(value, basestring))

    def test_words(self):
        value = self.sd.words()
        self.assertTrue(isinstance(value, basestring))
        self.assertTrue(len(value.split(' ')) >= 1)
        self.assertTrue(len(value.split(' ')) <= 5)

        value = self.sd.words(5, 5)
        self.assertTrue(len(value.split(' ')) == 5)

        self.assertEqual(self.sd.words(0, 0), '')

        with self.assertRaises(ParameterError):
            value = self.sd.words(10, 5)

    def test_email(self):
        value = self.sd.email()
        validate_email(value)

    def test_url(self):
        value = self.sd.url()
        URLValidator()(value)

    def test_sentence(self):
        for x in range(1, 10):
            value = self.sd.sentence()
            self.assertTrue(isinstance(value, basestring))
            self.assertTrue(len(value) <= 255)

    def test_short_sentence(self):
        for x in range(1, 10):
            value = self.sd.short_sentence()
            self.assertTrue(isinstance(value, basestring))
            self.assertTrue(len(value) <= 100)

    def test_long_sentence(self):
        for x in range(1, 10):
            value = self.sd.long_sentence()
            self.assertTrue(isinstance(value, basestring))
            self.assertTrue(len(value) >= 150)

    def test_paragraph(self):
        value = self.sd.paragraph()
        self.assertTrue(isinstance(value, basestring))

    def test_paragraphs(self):
        for x in range(1,10):
            value = self.sd.paragraphs()
            self.assertTrue(isinstance(value, basestring))

            self.assertTrue(len(value.split('\n\n')) >= 1)
            self.assertTrue(len(value.split('\n\n')) <= 5)

        with self.assertRaises(ParameterError):
            value = self.sd.paragraphs(5, 1)

    def test_slug(self):
        value = self.sd.slug()
        validate_slug(value)

        value = self.sd.slug(5, 5)
        self.assertEqual(len(value.split(' ')), 1)
        validate_slug(value)

        with self.assertRaises(ParameterError):
            value = self.sd.slug(10, 5)

    def test_tags(self):
        value = self.sd.tags()
        self.assertTrue(isinstance(value, basestring))

        value = self.sd.tags(5, 5)
        self.assertEqual(len(value.split(',')), 5)

        value = self.sd.tags(5, 5, ['a', 'b', 'c'])
        self.assertTrue(value.split(',')[0] in ['a', 'b', 'c'])

        with self.assertRaises(ParameterError):
            value = self.sd.tags(10, 5)

class TestTimeHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

    def test_date_between(self):
        value = self.sd.date_between(
                datetime.date(year=2000, month=1, day=1),
                datetime.date(year=2001, month=1, day=1),
        )
        self.assertTrue(isinstance(value, datetime.date))
        self.assertTrue(value > datetime.date(year=2000, month=1, day=1))
        self.assertTrue(value < datetime.date(year=2001, month=1, day=1))

        with self.assertRaises(ParameterError):
            self.sd.date_between(
                    datetime.date(year=2001, month=1, day=1),
                    datetime.date(year=2000, month=1, day=1),
            )

    #def test_future_date(self, min_distance=0, max_distance=365):
    #    pass

    #def test_past_date(self, min_distance=0, max_distance=365):
    #    pass

    def test_datetime_between(self):
        value = self.sd.datetime_between(
                datetime.datetime(year=2000, month=1, day=1),
                datetime.datetime(year=2001, month=1, day=1),
        )
        self.assertTrue(isinstance(value, datetime.datetime))
        self.assertTrue(value > datetime.datetime(year=2000, month=1, day=1))
        self.assertTrue(value < datetime.datetime(year=2001, month=1, day=1))

        with self.assertRaises(ParameterError):
            self.sd.datetime_between(
                    datetime.datetime(year=2001, month=1, day=1),
                    datetime.datetime(year=2000, month=1, day=1),
            )

    #def test_future_datetime(self, min_distance=0, max_distance=1440):
    #    pass

    #def test_past_datetime(self, min_distance=0, max_distance=1440):
    #    pass

    #def test_date(self, begin=-365, end=365):
    #    pass

    #def test_datetime(self, begin=-1440, end=1440):
    #    pass

class TestLocalizedHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

class TestImageHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

class TestOtherHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()
