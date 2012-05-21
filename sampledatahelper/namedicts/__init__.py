locales = ['es', 'en', 'ca', 'fr']

def get_names(locale):
    try:
        locale_mod = __import__("sampledatahelper.namedicts.%s" % locale)
        locale_mod = locale_mod.namedicts
        locale_mod = getattr(locale_mod, locale)
    except ImportError:
        raise Exception('Not valid locale')

    return [ x[0] for x in locale_mod.names ]

def all_names():
    names = []
    try:
        for locale in locales:
            locale_mod = __import__("sampledatahelper.namedicts.%s" % locale)
            locale_mod = locale_mod.namedicts
            locale_mod = getattr(locale_mod, locale)
            names += [ x[0] for x in locale_mod.names ]
    except ImportError:
        raise Exception('Not valid locale')

    return names

def get_surnames(locale):
    try:
        locale_mod = __import__("sampledatahelper.namedicts.%s" % locale)
        locale_mod = locale_mod.namedicts
        locale_mod = getattr(locale_mod, locale)
    except ImportError:
        raise Exception('Not valid locale')

    return [ x[0] for x in locale_mod.surnames ]

def all_surnames():
    surnames = []
    try:
        for locale in locales:
            locale_mod = __import__("sampledatahelper.namedicts.%s" % locale)
            locale_mod = locale_mod.namedicts
            locale_mod = getattr(locale_mod, locale)
            surnames += [ x[0] for x in locale_mod.surnames ]
    except ImportError:
        raise Exception('Not valid locale')

    return surnames

def get_names_number(locale):
    try:
        locale_mod = __import__("sampledatahelper.namedicts.%s" % locale)
        locale_mod = locale_mod.namedicts
        locale_mod = getattr(locale_mod, locale)
    except ImportError:
        raise Exception('Not valid locale')

    return locale_mod.names_number

def get_surnames_number(locale):
    try:
        locale_mod = __import__("sampledatahelper.namedicts.%s" % locale)
        locale_mod = locale_mod.namedicts
        locale_mod = getattr(locale_mod, locale)
    except ImportError:
        raise Exception('Not valid locale')

    return locale_mod.surnames_number
