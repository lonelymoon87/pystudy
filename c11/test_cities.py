# -*- coding: utf-8 -*
from c11 import full_city
import unittest

class CityTest(unittest.TestCase):
    '''测试城市全名'''
    def test_full_city(self):
        fullname = full_city("xiamen", "fujian")
        self.assertEqual(fullname, "Xiamen,Fujian")
    def test_population(self):
        fullname = full_city("xiamen", "fujian", population=1000)
        self.assertEqual(fullname, "Xiamen,Fujian-Population 1000")
unittest.main()
