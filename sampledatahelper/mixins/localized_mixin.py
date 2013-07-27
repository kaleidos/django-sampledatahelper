import random

from sampledatahelper.l10n.names import Name, Surname, FullName

from ..exceptions import ParameterError


class LocalizedMixin(object):
    def state_code(self, locale):
        """Random province code."""
        if locale == "es":
            return random.choice(
                ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                 '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                 '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                 '51', '52', 'AD', ]
            )
        elif locale == "us":
            return random.choice(
                ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
                 'AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI', ]
            )
        else:
            raise ParameterError("Not valid locale")

    def name(self, locale=None, number=None, as_list=False):
        return Name().generate(self, locale, number, as_list)

    def surname(self, locale=None, number=None, as_list=False):
        return Surname().generate(self, locale, number, as_list)

    def fullname(self, locale=None, as_list=False):
        return FullName().generate(self, locale, as_list)

    def phone(self, locale=None, country_code=False):
        phone = ''
        if locale == "es":
            if country_code is True:
                phone += "+34 "
            phone += random.choice(['6', '9'])
            phone += str(self.int(10000000, 99999999))
            return phone
        else:
            # Only works with implemented locales
            raise ParameterError("Not valid locale")

    def zip_code(self, locale=None):
        zip_code = ''
        if locale == "es":
            zip_code = "%05d" % self.int(1000, 52999)
            return zip_code
        else:
            # Only works with implemented locales
            raise ParameterError("Not valid locale")

    def id_card(self, locale=None):
        id_card = ''
        if locale == "es":
            id_card = "%05d" % self.int(1000, 52999)
            id_card = self.number_string(8)
            id_card_letters = "TRWAGMYFPDXBNJZSQVHLCKET"
            id_card += id_card_letters[int(id_card) % 23]
            return id_card
        else:
            # Only works with implemented locales
            raise ParameterError("Not valid locale")
