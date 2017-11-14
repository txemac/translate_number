# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from translator.number import number_translator


class TestNumber(unittest.TestCase):
    def __init__(self, test_name):
        super(TestNumber, self).__init__(test_name)

    def test_number_ok(self):
        num = 1234
        result = number_translator(num=num)
        self.assertEqual(result, '1,234')

    def test_number_small(self):
        num = 12
        result = number_translator(num=num)
        self.assertEqual(result, '12')

    def test_number_long(self):
        num = 123456789
        result = number_translator(num=num)
        self.assertEqual(result, '123,456,789')


if __name__ == '__main__':
    unittest.main()
