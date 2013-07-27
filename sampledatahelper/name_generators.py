from sampledatahelper.l10n import names

from .exceptions import ParameterError


class Name(object):
    def generate(self, sd, locale=None, number=None, as_list=False):
        if locale:
            names_list = names.get_names(locale)
            if number is None:
                number = names.get_names_number(locale)
        else:
            names_list = names.all_names()

        if number is None:
            number = 1

        if number < 1:
            raise ParameterError("number must be greater than 1")

        result = []
        for x in range(number):
            result.append(sd.choice(names_list))
        if as_list:
            return result
        else:
            return ' '.join(result)


class Surname(object):
    def generate(self, sd, locale=None, number=None, as_list=False):
        if locale:
            surnames = names.get_surnames(locale)
            if number is None:
                number = names.get_surnames_number(locale)
        else:
            surnames = names.all_surnames()

        result = []

        if number is None:
            number = 1

        if number < 1:
            raise ParameterError("number must be greater than 1")

        for x in range(number):
            result.append(sd.choice(surnames))

        if as_list:
            return result
        else:
            return ' '.join(result)


class FullName(object):
    def generate(self, sd, locale=None, as_list=False):
        sngen = Surname()
        ngen = Name()
        if locale:
            names_number = names.get_names_number(locale)
            surnames_number = names.get_surnames_number(locale)
        else:
            names_number = 1
            surnames_number = 1
        names_list = ngen.generate(sd, locale, names_number, True)
        surnames = sngen.generate(sd, locale, surnames_number, True)

        if as_list:
            return names_list+surnames
        else:
            return ' '.join(names_list+surnames)
