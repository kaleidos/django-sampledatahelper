#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

setup(
    name = 'django-sampledatahelper',
    version = ":versiontools:sampledatahelper:",
    description = "Helper class for generate sampledata",
    long_description = "",
    keywords = 'django, data, example',
    author = 'Jesús Espino García',
    author_email = 'jespinog@gmail.com',
    url = 'https://github.com/kaleidos/django-sampledatahelper',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    package_data={
        'sampledatahelper': [
            'static/*',
        ]
    },
    install_requires=[
        'six',
        'django',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    test_suite = 'nose.collector',
    tests_require = ['nose >= 1.2.1', 'django >= 1.3.0'],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
