# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:31:49 2021

@author: Администратор
"""

import unittest
from list_title import royxat_title
a = ['sad','saddf','dfg']

class RoyxatTest(unittest.TestCase):
    def test_list(self):
        r = royxat_title(a)
        self.assertEqual(r,['Sad', 'Saddf', 'Dfg'])
unittest.main()
