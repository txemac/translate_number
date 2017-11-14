# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from translator.number import number_translator


num = input("Insert the number please: ")

result = number_translator(num=num)

print result
