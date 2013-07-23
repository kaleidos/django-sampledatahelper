API
===

Number methods
--------------

.. function:: int(min_value=0, max_value=sys.maxint)

    Return an integer between min_value and max_value

.. function:: number(ndigits)

    Return a number of n digits as max

.. function:: digits(ndigits)

    Return a number of exactly n digits

.. function:: float(min, max)

    Return a float from min to max

.. function:: number_string(ndigits)

    Return a string of n digits

Text methods
------------

.. function:: char()

    Return a character between A-Z and a-z

.. function:: chars(min_chars=1, max_chars=5)

    Return a string with n characters between A-Z and a-z being
    min_chars <= n <= max_chars

.. function:: word()

    Returns a lorem ipsum word

.. function:: words(min_words=1, max_words=5)

    Return a string with n lorem ipsum words being
    min_words <= n <= max_words

.. function:: email()

    Return an email

.. function:: url()

    Return an url

.. function:: sentence()

    Return a lorem ipsum sentence (limited to 255 caracters)

.. function:: short_sentence()

    Return a lorem ipsum sentence (limited to 100 caracters)

.. function:: long_sentence()

    Return a lorem ipsum sentence (with 150 caracters or more)

.. function:: paragraph()

    Return a lorem ipsum paragraph

.. function:: paragraphs(min_paragraphs=1, max_paragraphs=5)

    Return a lorem ipsum text with n paragraphs being
    min_paragraphs <= n <= max_paragraphs

.. function:: slug(min_words=5, max_words=5)

    Return a lorem ipsum slug between with n words being
    min_words <= n <= max_words

.. function:: tags(min_tags=1, max_tags=5, tags_list=None)

    Return a string of n tags_list or lorem ipsum tags separated by commas
    being n max min_tags <= n <= max_tags

Time methods
------------

.. function:: date(begin=-365, end=365)

    Return a date between now+begin and now+end in days

.. function:: date_between(min_date, max_date)

    Return a date between the min_date and max_date date objects

.. function:: future_date(min_distance=0, max_distance=365)

    Return a future date between now+min_distance and now+max_distance in days

.. function:: past_date(min_distance=0, max_distance=365)

    Return a past date between now-max_distance and now-min_distance in days

.. function:: datetime(begin=-1440, end=1440)

    Return a datetime between now+begin and now+end in minutes

.. function:: datetime_between(min_datetime, max_datetime)

    Return a datetime between the min_datetime and max_datetime datetime objects

.. function:: future_datetime(min_distance=0, max_distance=1440)

    Return a future datetime between now+min_distance and now+max_distance in minutes

.. function:: past_datetime(min_distance=0, max_distance=1440)

    Return a past datetime between now-max_distance and now-min_distance in minutes

Localized methods
-----------------

.. function:: name(locale=None, number=1, as_list=False)

    Return a string or list of tipical names from locale using n names (compound names)

    Supported locales: es

.. function:: surname(locale=None, number=1, as_list=False)

    Return a string or list of tipical surnames from locale using n surnames

    Supported locales: es

.. function:: fullname(locale=None, as_list=False)

    Return a string or list of tipical names+surnames from locale

    Supported locales: es

.. function:: phone(locale, country_code)

    Return a phone number from a country with or without country code

    Supported locales: es

.. function:: zip_code(locale)

    Return a zip code for a country

    Supported locales: es

.. function:: state_code(locale)

    Return a state code for the locale country.

    Supported locales: es

.. function:: id_card(locale)

    Return a identification card code for a country

    Supported locales: es

Image methods
-------------

.. function:: image(width, height, typ="simple")

    Return an image of width x height size generated with the typ generator.

    Available typ generators: simple, plasma, mandelbrot, ifs, random

.. function:: image_from_directory(directory_path, valid_extensions=['.jpg', '.bmp', '.png'])

    Return an image from a directory with a valid extension

Other methods
-------------

.. function:: boolean()

    Return a boolean value

.. function:: choice(choices)

    Return a value from a list

.. function:: choices_key(choices)

    Return a key from a django choices list

.. function:: db_object(model)

    Return a random object from the model

.. function:: db_object_from_queryset(queryset)

    Return a random object from the queryset
