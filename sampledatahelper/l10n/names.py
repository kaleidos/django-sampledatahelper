import json
import os.path

from sampledatahelper.exceptions import ParameterError

LOCALES = ['es', 'us', 'cat', 'fr']
NAMES_PATH = os.path.join(os.path.dirname(__file__), 'names')


class Name(object):
    data = {}

    def __load_locale(self, locale):
        locale_path = os.path.join(NAMES_PATH, "{0}.json".format(locale))
        if not os.path.exists(locale_path):
            raise ParameterError('Not valid locale')

        Name.data[locale] = json.load(open(locale_path, 'r'))

    def get_names(self, locale):
        if locale not in Name.data:
            self.__load_locale(locale)

        return [x[0] for x in Name.data[locale]['names']]

    def get_names_number(self, locale):
        if locale not in Name.data:
            self.__load_locale(locale)

        return Name.data[locale]['names_number']

    def all_names(self):
        names = []
        for locale in LOCALES:
            names += self.get_names(locale)

        return names

    def generate(self, sd, locale=None, number=None, as_list=False):
        if locale:
            names = self.get_names(locale)
            if number is None:
                number = self.get_names_number(locale)
        else:
            names = self.all_names()

        if number is None:
            number = 1

        if number < 1:
            raise ParameterError("number must be greater than 1")

        result = []
        for x in range(number):
            result.append(sd.choice(names))

        if as_list:
            return result

        return ' '.join(result)


class Surname(object):
    data = {}

    def __load_locale(self, locale):
        locale_path = os.path.join(NAMES_PATH, "{0}.json".format(locale))
        if not os.path.exists(locale_path):
            raise ParameterError('Not valid locale')

        Surname.data[locale] = json.load(open(locale_path, 'r'))

    def get_surnames(self, locale):
        if locale not in Surname.data:
            self.__load_locale(locale)

        return [x[0] for x in Surname.data[locale]['surnames']]

    def get_surnames_number(self, locale):
        if locale not in Surname.data:
            self.__load_locale(locale)

        return Surname.data[locale]['surnames_number']

    def all_surnames(self):
        surnames = []
        for locale in LOCALES:
            surnames += self.get_surnames(locale)

        return surnames

    def generate(self, sd, locale=None, number=None, as_list=False):
        if locale:
            surnames = self.get_surnames(locale)
            if number is None:
                number = self.get_surnames_number(locale)
        else:
            surnames = self.all_surnames()

        result = []

        if number is None:
            number = 1

        if number < 1:
            raise ParameterError("number must be greater than 1")

        for x in range(number):
            result.append(sd.choice(surnames))

        if as_list:
            return result

        return ' '.join(result)


class FullName(object):
    def generate(self, sd, locale=None, as_list=False):
        sngen = Surname()
        ngen = Name()

        names_number = 1
        surnames_number = 1

        if locale:
            names_number = ngen.get_names_number(locale)
            surnames_number = sngen.get_surnames_number(locale)

        names = ngen.generate(sd, locale, names_number, True)
        surnames = sngen.generate(sd, locale, surnames_number, True)

        if as_list:
            return names + surnames

        return ' '.join(names + surnames)
