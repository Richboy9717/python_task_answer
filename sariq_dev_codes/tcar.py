# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 08:36:00 2021

@author: Администратор
"""

class Avto:
    def __init__(self,model,rang,yili,narh=None):
        self.model = model
        self.rang = rang
        self.yili = yili
        self.__km = 0
        self.narh = narh

    def get_info(self):
        return f'Model: {self.model} Rangi: {self.rang} Yili: {self.yili} Narxi: {self.narh} Km: {self.__km}'

    def add_km(self,kilometr):
        self.__km +=kilometr
        
    def get_km(self):
        return self.__km
    
    def __repr__(self):
        return self.model

avto1 = Avto('Hyundai','Silver',2020,2000)

avto1.add_km(300)
avto1.add_km(400)

