# import unittest
# from shaxs_class import Shaxs
# class ShTest(unittest.TestCase):
#     def setUp(self):
#         ism = 'Aziz'
#         familya = 'Lazizov'
#         tyil = 1999
#         self.pasport = 'AA0090910'
#         self.shaxs1 = Shaxs(ism,familya,tyil,self.pasport)
#     def test_shaxs(self):
#         self.assertIsNotNone(self.shaxs1.ism)
#         self.assertIsNotNone(self.shaxs1.fam)
#         self.assertIsNotNone(self.shaxs1.tyil)
#         self.assertIsNotNone(self.shaxs1.pasport)
#
#     def test_get_age(self):
#         self.assertEqual(22,self.shaxs1.get_age())
#
#     def test_get_info(self):
#         self.assertEqual('Ism: Aziz Familya: Lazizov Passport: AA0090910',self.shaxs1.get_info())
#
#
#
#
#
# unittest.main()

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:52:54 2021

@author: Администратор
"""

class Queue:
    def __init__(self):
        self.elements = []

    def enque(self, element):
        return self.elements.append(element)

    def deque(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)





