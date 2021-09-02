# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:46:43 2021

@author: Администратор
"""

import unittest
from shaxs_class import Shaxs
class ShTest(unittest.TestCase):
    def setUp(self):
        ism = 'Aziz'
        familya = 'Lazizov'
        tyil = 1999
        self.pasport = 'AA0090910'
        self.shaxs1 = Shaxs(ism,familya,tyil,self.pasport)
    def test_shaxs(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.fam)
        self.assertIsNotNone(self.shaxs1.tyil)
        self.assertIsNotNone(self.shaxs1.pasport)
    
    def test_get_age(self):
        self.assertEqual(22,self.shaxs1.get_age(2021))
        
    
    def test_get_info(self):
        self.assertEqual('Ism: Aziz Familya: Lazizov Passport: AA0090910',self.shaxs1.get_info())


unittest.main()
