SECRET_KEY = "123"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': ':memory:',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'sampledatahelper',
    'tests'
]

MIDDLEWARE_CLASSES = [] # Just to avoid a warning

ALLOWED_HOSTS = ['testserver',]

BACKEND_SESSION_KEY = "test"

USE_TZ = True

SAMPLEDATAHELPER_MODELS = [
    {
        'model': 'tests.TestRelatedModel',
        'number': 10,
    },
    {
        'model': 'tests.TestModel',
        'number': 5,
        'fields_overwrite': [
            ('small_integer', lambda _, sd: sd.int(1, 10)),
            ('integer', lambda instance, _: instance.small_integer * 2),
            ('positive_integer', 8),
        ]
    }
]
