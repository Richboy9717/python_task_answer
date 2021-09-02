# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:29:48 2021

@author: Администратор
"""

# Matnlardan iborat ro'yxat qabul qilib,
# ro'yxatdagi har bir matnning birinchi
# harfini katta harfga o'zgatiruvchi funksiya
a = ['sad','saddf','dfg']

def royxat_title(royxat):
    return [x.title() for x in royxat]