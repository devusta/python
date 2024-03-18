# -*- coding: utf-8 -*-
"""
45-video
37-dars. KLASSLARNI TEKSHIRISH
Created on Sun Mar 17 21:16:15 2024

@author: Asadbek (devusta)
"""
# ✅NEW UNDERSTANDINGS
# raise - sun'iy ravishda xatoni keltirib chiqarish
# setUp - classni test qilishda test uchun xususiyatlar berish funksiyasi

class Car:
    def __init__(self, maker, model, year, km=0, price=None):
        self.maker = maker
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
        
    def set_price(self, price):
        self.price = price
        
    def add_km(self, km):
        if km > 0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas.")
    
    def get_info(self):
        info = f"{self.maker.upper()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km} km yurgan."
        if self.price:
            info += f" Narxi: {self.price}"
        return info
    
    def get_km(self):
        return self.__km


# auto = Car('gm', 'malibu', 1290)
# auto.add_km(-188)
























