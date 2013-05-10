import math
from sampledatahelper import namedicts

class Name(object):
    def generate(self, sd, locale=None, number=1, as_dict=False):
        if locale:
            names = namedicts.get_names(locale)
        else:
            names = namedicts.all_names()

        result = []
        for x in range(number):
            result.append(sd.choice(names))
        if as_dict:
            return result
        else:
            return ' '.join(result)


class Surname(object):
    def generate(self, sd, locale=None, number=1, as_dict=False):
        if locale:
            surnames = namedicts.get_surnames(locale)
        else:
            surnames = namedicts.all_surnames()

        result = []
        for x in range(number):
            result.append(sd.choice(surnames))

        if as_dict:
            return result
        else:
            return ' '.join(result)

class FullName(object):
    def generate(self, sd, locale=None, as_dict=False):
        sngen = Surname()
        ngen = Name()
        if locale:
            names_number = namedicts.get_names_number(locale)
            surnames_number = namedicts.get_surnames_number(locale)
        else:
            names_number = 1
            surnames_number = 1
        names = ngen.generate(sd, locale, names_number, True)
        surnames = sngen.generate(sd, locale, surnames_number, True)

        if as_dict:
            return names+surnames
        else:
            return ' '.join(names+surnames)
