#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sampledatahelper

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
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
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
