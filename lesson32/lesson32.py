# -*- coding: utf-8 -*-
"""
40-video
32-dars. DUNDER METODLAR

Created on Sun Feb 25 22:35:01 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # dir() - obyektning maxsus xususiyatlarini ko'rish uchun funksiya
# # __str__() - obyekt haqida ma'lumot olish. Faqat str va print bilan ishlaydi
# # __repr__() - obyekt haqida ma'lumot olish metodi. Barcha ma'lumot turlari bilan ishlaydi
# # __len__() - obyektning uzuligi
# # __getitem__() - 
# # __setitem__() - 
# # __call__() - obyekt haqida ma'lumot olish metodi
# # __lt__(self, y) - x < y
# # __le__(self, y) - x <= y 
# # __gt__(self, y) - x > y
# # __ge__(self, y) - x >= y
# # __eq__(self, y) - x == y
# # __ne__(self, y) - x != y
# # isinstance() - obyektni qandaydir klassga tegishli yoki yo'qligini tekshirish
# # __getitem__() - ro'yxatdagi ma'lum elementni ko'rish
# # __setitem__() - ro'yxatga ma'lum element qo'shish
# # __call__() 
# # __add__()
# # __sub__()
# =============================================================================


from auto import Auto, AutoSalon
                
                
auto1 = Auto('GM', 'Malibu', 'black', 2023, 30000)
auto2 = Auto('Kia', 'K8', 'silver', 2024, 34000)
auto3 = Auto('Hyundai', 'Sonata', 'white', 2024, 29000)
auto4 = Auto('Nissan', 'Nata', 'black', 2020, 23000)
auto5 = Auto('Toyota', 'Jiku', 'silver', 2019, 24000)

# print(auto1 == auto2)
# print(auto1 != auto2)
# print(auto1 < auto2)
# print(auto1 > auto2)
# print(auto1 <= auto2)
# print(auto1 >= auto2)
                
salon1 = AutoSalon('AutoBox')
salon2 = AutoSalon('BigAuto')

salon1.add_auto(auto1, auto2, auto3)
# print(len(salon1)) # len list
# print(salon1[0])   # get item
# print(salon1[:])

# set item
salon1[0] = Auto('Audi', 'A7', 'black', 2024, 37000)
# print(salon1[:])

salon1()  # __call__ test

salon3 = salon1 + salon2   # __add__ test
# print(salon3)
# print(salon3(auto4, auto5))

print(salon1())   # __add__ test
salon1(auto5)
print(salon1())








































