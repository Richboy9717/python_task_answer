# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:43:19 2021

@author: Администратор
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_name(self):
        name = get_full_name('alijon','valiyev')
        self.assertEqual(name,'Alijon Valiyev')
unittest.main()