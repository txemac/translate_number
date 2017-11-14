# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def number_translator(num):
    """
    Return a string representation of that integer with commas separating groups of 3 digits.

    :param num: integer
    :return: string
    """
    return '{0:,}'.format(num)
