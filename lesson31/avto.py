# -*- coding: utf-8 -*-
"""
39-video
31-dars. INKAPSULATSIYA VA KLASSGA OID XUSUSIYAT METODLAR 
Created on Sun Feb 25 14:42:31 2024

@author: Asadbek (devusta)
"""
                    # MODUL FAYL

# TAKRORLANMAYDIGAN ID GENERATSIYA QILIB BERRUVCHI FUNKSIYA
from uuid import uuid4

# =============================================================================
# # OBYEKTLAR UCHUN INKAPSULATSIYA XUSUSIYAT
# class Auto:
#     """Avtomobil klassi"""
#     def __init__(self, maker, model, color, year, price, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.maker = maker
#         self.model = model
#         self.color = color
#         self.price = price
#         self.__km = km       # INKAPSULATSIYA XUSUSIYAT
#         self.__id = uuid4()  # INKAPSULATSIYA XUSUSIYAT
#     
#     def get_km(self):
#         return self.__km
#     
#     def get_id(self):
#         return self.__id
#     
#     def add_km(self, km):
#         """Mashina km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km ni kamaytirib bo'lmaydi.")
#             
# avto1 = Auto('GM', 'Malibu', 'black', 2022, 30000, 1000)
# 
# print(auto1.maker)
# auto1.add_km(1300)
# auto1.add_km(-1000)
# print(auto1.get_km())
# =============================================================================

# KLASSLAR UCHUN INKAPSULATSIYA XUSUSIYAT
class Auto:
    """Avtomobil klassi"""
    __num_auto = 0   # KLASSNING INKAPSULATSIYA XUSUSIYATI
    def __init__(self, maker, model, color, year, price, km=0):
        """Obyektlarning xususiyatlari"""
        self.maker = maker
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km        # OBYEKTNING XUSUSIYATI
        self.__id = uuid4()   # OBYEKTNING XUSUSIYATI
        Auto.__num_auto += 1  # KLASSNING XUSUSIYATI

    @classmethod 
    def get_num_auto(cls):
        return cls.__num_auto # Klassning xususiyatini olish
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km ni kamaytirib bo'lmaydi.")



# Faylda klasslar soni ko'p bo'lsa funksiyalar kabi alohida modulda 
# saqlash lozim!








































