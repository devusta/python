# -*- coding: utf-8 -*-
"""
11-video
8-dars. RO'YXATLAR BILAN ISHLASH. O'ZGARMAS RO'YXATLAR

Created on Sat Feb 10 17:29:35 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # SORT(), REVERSE
# cars = ['bmw', 'volvo', 'nissan', 'toyoto', 'audi', 'mers', 'hyundai', 'kia']
# 
# cars.sort() # list elementlarini alifbo tartibida tartiblash
# cars.sort(reverse=True) # list elementlarini alifbo tartibiga teskari tarzda tartiblash
# =============================================================================

# =============================================================================
# # SORTED(), REVERSE()
# cars = ['bmw', 'volvo', 'nissan', 'toyoto', 'audi', 'mers', 'hyundai', 'kia']
# print(sorted(cars)) # list elementlarini asl tartibiga tegmagan holatda 
#                     # alifbo tartibida ekranga chiqarish
# 
# print(sorted(cars, reverse=True)) # list elementlarini asl tartibini o'zgartirmagan
#                                   # holda alifbo tartibiga teskari tartibda ekranga chiqarish
# cars.reverse() # list elementlarini asl tartibga teskari tartibda saqlash 
# 
# print(len(cars)) # listning uzunligini aniqlash
# =============================================================================

# =============================================================================
# # RANGE()
# sonlar = list(range(0, 10)) # ma'lum bir oraliqdagi sonlardan list yaratish
# 
# toq_sonlar = list(range(1, 19, 2)) # toq sonlar ro'yxatini yaratish
# 
# juft_sonlar = list(range(2, 20, 2)) # juft sonlar listini yaratish
# 
# ontalik_sonlar = list(range(10, 101, 10))
# max_qiymat = max(ontalik_sonlar) # listdagi eng katta qiymatni topish
# =============================================================================

# =============================================================================
# # MIN(), MAX(), SUM()
# narxlar = [23000, 3200, 45000, 4560, 1100, 35000]
# eng_arzon = min(narxlar)
# eng_qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narx ", eng_arzon, "so'm, eng qimmat narx ", eng_qimmat, "so'm, jami ", jami, "so'm.")
# 
# print("Eng arzon narx ", min(narxlar), "so'm, eng qimmat narx ", max(narxlar), "so'm, jami ", sum(narxlar), "so'm.")
# print(max(narxlar))
# =============================================================================

# =============================================================================
# # LISTNI KESISH
# cars = ['bmw', 'volvo', 'nissan', 'toyoto', 'audi', 'mers', 'hyundai', 'kia']
# print(cars[0:3]) # listni 0-indeksidan 3-indeksigacha olish
# print(cars[3:6]) # listni 3-indeksidan 6-indeksigacha olish
# print(cars[:4]) # birinchi qiymat berilmaganda o'z-o'zidan 0dan boshlanadi
# print(cars[3:]) # oxirgi element berilmaganda ham o'z-o'zidan oxirigacha olinadi
# print(cars[4:-1])
# =============================================================================

# =============================================================================
# # LISTDAN NUSXA OLISH
# cars = ['bmw', 'volvo', 'nissan', 'toyoto', 'audi', 'mers', 'hyundai', 'kia']
# my_cars = cars[:]
# my_cars.remove('bmw')
# del my_cars[3]
# 
# print(my_cars)
# =============================================================================

# =============================================================================
# # TUPLE - O'ZGARMAS RO'YXAT
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[3:5])
# print(toys[-1])
# print(toys[3:])
# print(type(toys))
# 
# toys = list(toys) # tuple turidagi ro'yxatni listga o'zgartirish
# print(type(toys))
# 
# toys = tuple(toys) # list turidagi ro'xyatni tuple ga o'zgartish
# print(type(toys))
# =============================================================================
























