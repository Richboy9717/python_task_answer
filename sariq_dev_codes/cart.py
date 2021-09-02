# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:45:33 2021

@author: Администратор
"""

import unittest
from tcar import Avto
class CarTest(unittest.TestCase):
    def setUp(self):
        model = 'Malibu'
        rang = 'Qora'
        yili = 2020
        self.narhi = 10000
        self.avto1 = Avto(model,rang,yili)
        self.avto2 = Avto(model, rang, yili,narh=self.narhi)

    def test_xususiyat(self):
        #Ichida Qiymat borligini tekshiradi
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.rang)
        self.assertIsNotNone(self.avto1.yili)
        #Ichida qiymat yo'qligini tekshiradi
        self.assertIsNone(self.avto1.narh)
        #km 0 ga teng ekanini tekshiradi
        self.assertEqual(0,self.avto1.get_km())
        #avto2 ni narhini tekshiramiz
        self.assertEqual(self.narhi,self.avto2.narh)
    
    def test_set_km(self):
        self.avto1.add_km(3000)
        n = self.avto1.get_km()
        self.assertEqual(3000,self.avto1.get_km())
unittest.main()
