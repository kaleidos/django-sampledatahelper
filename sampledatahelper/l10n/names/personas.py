#!/usr/bin/env python
# -*- coding: UTF-8 -*-



TWO_FAMILY_NAMES = ('es','ca')

import random

_random_name = lambda lang='es':random.choice(globals()['nombres_%s' % lang]).capitalize()
_random_surname = lambda lang='es':random.choice(globals()['apellidos_%s' % lang]).capitalize()

def person(lang='es'):
    u"""
    Retuns a tuple with person name and two surnames
    u"""
    return (unicode(_random_name(lang),"utf-8"), unicode(_random_surname(lang),"utf-8"),
            unicode(_random_surname(lang),"utf-8") if lang in TWO_FAMILY_NAMES else u"")

def person_fullname(lang='es'):
    return u" ".join(person(lang))

if __name__=='__main__':
    for i in range(0, 10):
        print person_fullname()


