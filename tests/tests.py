from django.utils import unittest
from django.core.validators import validate_email, validate_slug, URLValidator
from django.utils.timezone import utc

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

    def test_future_date(self, min_distance=0, max_distance=365):
        value = self.sd.future_date()
        self.assertTrue(isinstance(value, datetime.date))

        self.assertTrue(value >= datetime.date.today())
        self.assertTrue(value <= (datetime.date.today() + datetime.timedelta(days=365)))

        value = self.sd.future_date(0, 10)
        self.assertTrue(value >= datetime.date.today())
        self.assertTrue(value <= (datetime.date.today() + datetime.timedelta(days=10)))

        with self.assertRaises(ParameterError):
            self.sd.future_date(100, 0)

        with self.assertRaises(ParameterError):
            self.sd.future_date(-10, 10)

    def test_past_date(self, min_distance=0, max_distance=365):
        value = self.sd.past_date()
        self.assertTrue(isinstance(value, datetime.date))

        self.assertTrue(value <= datetime.date.today())
        self.assertTrue(value >= (datetime.date.today() - datetime.timedelta(days=365)))

        value = self.sd.past_date(0, 10)
        self.assertTrue(value <= datetime.date.today())
        self.assertTrue(value >= (datetime.date.today() - datetime.timedelta(days=10)))

        with self.assertRaises(ParameterError):
            self.sd.past_date(100, 0)

        with self.assertRaises(ParameterError):
            self.sd.past_date(-10, 10)

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

    def test_future_datetime(self, min_distance=0, max_distance=1440):
        value = self.sd.future_datetime()
        self.assertTrue(isinstance(value, datetime.datetime))

        self.assertTrue(value >= datetime.datetime.utcnow().replace(tzinfo=utc))
        self.assertTrue(value <= (datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(minutes=1440)))

        value = self.sd.future_datetime(0, 10)
        self.assertTrue(value >= datetime.datetime.utcnow().replace(tzinfo=utc))
        self.assertTrue(value <= (datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(minutes=10)))

        with self.assertRaises(ParameterError):
            self.sd.future_datetime(100, 0)

        with self.assertRaises(ParameterError):
            self.sd.future_datetime(-10, 10)

    def test_past_datetime(self, min_distance=0, max_distance=1440):
        value = self.sd.past_datetime()
        self.assertTrue(isinstance(value, datetime.datetime))

        self.assertTrue(value <= datetime.datetime.utcnow().replace(tzinfo=utc))
        self.assertTrue(value >= (datetime.datetime.utcnow().replace(tzinfo=utc) - datetime.timedelta(minutes=1440)))

        value = self.sd.past_datetime(0, 10)
        self.assertTrue(value <= datetime.datetime.utcnow().replace(tzinfo=utc))
        self.assertTrue(value >= (datetime.datetime.utcnow().replace(tzinfo=utc) - datetime.timedelta(minutes=10)))

        with self.assertRaises(ParameterError):
            self.sd.past_datetime(100, 0)

        with self.assertRaises(ParameterError):
            self.sd.past_datetime(-10, 10)


    def test_date(self):
        value = self.sd.date()
        self.assertTrue(isinstance(value, datetime.date))

        self.assertTrue(value >= (datetime.date.today() - datetime.timedelta(days=365)))
        self.assertTrue(value <= (datetime.date.today() + datetime.timedelta(days=365)))

        value = self.sd.date(-10, 10)
        self.assertTrue(value >= (datetime.date.today() - datetime.timedelta(days=10)))
        self.assertTrue(value <= (datetime.date.today() + datetime.timedelta(days=10)))

        with self.assertRaises(ParameterError):
            self.sd.date(100, 0)

    def test_datetime(self):
        value = self.sd.datetime()
        self.assertTrue(isinstance(value, datetime.datetime))

        self.assertTrue(value >= (datetime.datetime.utcnow().replace(tzinfo=utc) - datetime.timedelta(minutes=1440)))
        self.assertTrue(value <= (datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(minutes=1440)))

        value = self.sd.datetime(-10, 10)
        self.assertTrue(value >= (datetime.datetime.utcnow().replace(tzinfo=utc) - datetime.timedelta(minutes=10)))
        self.assertTrue(value <= (datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(minutes=10)))

        with self.assertRaises(ParameterError):
            self.sd.datetime(100, 0)

class TestLocalizedHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

    def test_state_code(self):
        value = self.sd.state_code('es')
        self.assertTrue(value in ['01', '02', '03', '04', '05', '06', '07',
                                  '08', '09', '10', '11', '12', '13', '14',
                                  '15', '16', '17', '18', '19', '20', '21',
                                  '22', '23', '24', '25', '26', '27', '28',
                                  '29', '30', '31', '32', '33', '34', '35',
                                  '36', '37', '38', '39', '40', '41', '42',
                                  '43', '44', '45', '46', '47', '48', '49',
                                  '50', '51', '52', 'AD', ])

        value = self.sd.state_code('us')
        self.assertTrue(value in ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT',
                                  'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
                                  'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
                                  'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV',
                                  'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
                                  'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN',
                                  'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
                                  'WY', 'AS', 'DC', 'FM', 'GU', 'MH', 'MP',
                                  'PW', 'PR', 'VI', ])

        with self.assertRaises(ParameterError):
            self.sd.state_code('invalid-code')

    def test_name(self):
        value = self.sd.name()
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        value = self.sd.name(as_list=True)
        self.assertTrue(isinstance(value, list))
        self.assertEqual(len(value), 1)

        value = self.sd.name(number=3)
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 3)

        value = self.sd.name(number=3, as_list=True)
        self.assertTrue(isinstance(value, list))
        self.assertEqual(len(value), 3)

        value = self.sd.name(locale='es')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        value = self.sd.name(locale='ca')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        value = self.sd.name(locale='fr')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        value = self.sd.name(locale='us')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        with self.assertRaises(ParameterError):
            value = self.sd.name(number=0)

        with self.assertRaises(ParameterError):
            value = self.sd.name(number=-1)

        with self.assertRaises(ParameterError):
            value = self.sd.name(locale="not-valid-locale")

    def test_surname(self):
        value = self.sd.surname()
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        value = self.sd.surname(as_list=True)
        self.assertTrue(isinstance(value, list))
        self.assertEqual(len(value), 1)

        value = self.sd.surname(number=3)
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 3)

        value = self.sd.surname(number=3, as_list=True)
        self.assertTrue(isinstance(value, list))
        self.assertEqual(len(value), 3)

        value = self.sd.surname(locale='es')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 2)

        value = self.sd.surname(locale='ca')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 2)

        value = self.sd.surname(locale='fr')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        value = self.sd.surname(locale='us')
        self.assertTrue(isinstance(value, basestring))
        self.assertEqual(len(value.split(' ')), 1)

        with self.assertRaises(ParameterError):
            value = self.sd.surname(number=0)

        with self.assertRaises(ParameterError):
            value = self.sd.surname(number=-1)

        with self.assertRaises(ParameterError):
            value = self.sd.surname(locale="not-valid-locale")

    #def fullname(self, locale=None, as_list=False):
    #    return FullName().generate(self, locale, as_list)

    #def phone(self, locale=None, country_code=False):
    #    phone = ''
    #    if locale == "es":
    #        if country_code is True:
    #            phone += "+34 "
    #        phone += random.choice(['6', '9'])
    #        phone += str(self.int(10000000, 99999999))
    #        return phone
    #    else:
    #        # Only works with implemented locales
    #        raise NotImplemented

    #def zip_code(self, locale=None):
    #    zip_code = ''
    #    if locale == "es":
    #        zip_code = "%05d" % self.int(1000, 52999)
    #        return zip_code
    #    else:
    #        # Only works with implemented locales
    #        raise NotImplemented

    #def id_card(self, locale=None):
    #    id_card = ''
    #    if locale == "es":
    #        id_card = "%05d" % self.int(1000, 52999)
    #        id_card = self.number_string(8)
    #        id_card_letters = "TRWAGMYFPDXBNJZSQVHLCKET"
    #        id_card += id_card_letters[int(id_card) % 23]
    #        return id_card
    #    else:
    #        # Only works with implemented locales
    #        raise NotImplemented

class TestImageHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()

class TestOtherHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sd = SampleDataHelper()
