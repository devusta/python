# -*- coding: utf-8 -*-
"""
27-video
24-dars. lAMBDA - NOMSIZ FUNKSIYALAR
Created on Sun Feb 18 08:31:58 2024

@author: Asadbek (devusta)
"""
import math
# =============================================================================
# # LAMBDA FUNKSIYA YARATISH
# # Lambda funksiyada bir nechta argument va faqatgina bitta ifoda bo'ladi
# # 1
# aylana_uzunlik = lambda pi, r: 2*pi*r
# print(aylana_uzunlik(math.pi, 10))
# 
# # 2
# kvadrat = lambda x, y: x ** y
# print(kvadrat(3, 2))
# =============================================================================

# =============================================================================
# # LAMBDA FUNKSIYADAN FOYDALANISH
# def daraja(n):
#     """O'zida lambda funksiya saqlovchi odatiy funksiya"""
#     return lambda x: x**n # lambda funksiya
# 
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 ning kvadrati {kvadrat(3)} ga, "
#       f"kubi esa {kub(3)} ga teng.")
# =============================================================================

# =============================================================================
# # MAP FUKSIYASI & SQRT FUKSIYASI
# from math import sqrt # sqrt - kvadrat ildizni qaytaruvchi funksiya
# 
# # 1
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)
# 
# # 2
# raqamlar = list(range(5, 15))
# def kvadrat(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(kvadrat, raqamlar)))
# =============================================================================

# =============================================================================
# # MAP & LAMBDA / LAMBDA FUNKSIYASINING QULAYLIGI
# sonlar = list(range(11))
# print(list(map(lambda x: x*x, sonlar)))
# =============================================================================

# =============================================================================
# # MAP & LAMBDA
# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y: x+y, a, b))
# print(a_plus_b)
# =============================================================================

import random as r
# =============================================================================
# # SAMPLE function FROM RANDOM
# # FILTER FUNKSIYASI
# sonlar = r.sample(range(100), 10) # 0-99 oralig'ida 10 ta tasodifiy son qaytaradi
# print(sonlar)
# def juftmi(x):
#     """x juft bo'lsa True, toq bo'lsa False qaytaruvchi funksiya"""
#     return x % 2 == 0
# # print(juftmi(7)) # sonni juft yoki toqligini aniqlash
# 
# juft_sonlar = list(filter(juftmi, sonlar)) # listdagi sonlardan juftlarini olish
# print(juft_sonlar)
# =============================================================================

# =============================================================================
# # LAMBADA $ FILTER
# # LAMBDA FUNKSIYASI ORQALI YUQORIDAGI KODNI QISQAROQ YOZISH
# sonlar = r.sample(range(100), 10)
# print(sonlar)
# 
# juft_sonlar = list(filter(lambda x: x%2==0, sonlar))
# print(juft_sonlar)
# =============================================================================

# =============================================================================
# # BOSH HARFNI ANIQLASH
# talabalar = ['olim', 'akmal', 'bahrom', 'azam', 'bobomirza', 'kozim', 'ilhom', 'mirza', 'hoshim', 'bobur', 'farhod', 'shamshod', 'kamol']
# talabalar_a = []
# talabalar_b = []
# for talaba in talabalar:
#     b_harf_a = talaba.startswith('a')
#     if b_harf_a is True:
#         talabalar_a.append(talaba)
#     b_harf_b = talaba.startswith('b')
#     if b_harf_b is True:
#         talabalar_b.append(talaba)
# 
# print(talabalar)
# print(talabalar_a)
# print(talabalar_b)
# =============================================================================

# =============================================================================
# # ODDIY FUNKSIYA ORQALI BOSH HARFNI ANIQLASH
# def boshHarf(element, harf):
#     """Matnning bosh harfini aniqlab True/False qiymat qaytaruvchi funksiya"""
#     return element.startswith(harf)
#   
#     
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'behi', 'banan', 'gilos']
# mevalar_b = []
# mevalar_a = []
# for n in mevalar:      
#     bosh_a = (boshHarf(n, 'a'))
#     bosh_b = (boshHarf(n, 'b'))
#     if bosh_a is True:
#         mevalar_a.append(n)
#     elif bosh_b is True:
#         mevalar_b.append(n)
# 
# print(mevalar)
# print(mevalar_a)
# print(mevalar_b)
# =============================================================================
       
# =============================================================================
# # LAMBDA & FILTER
# # LAMBDA FUNKSIYASI ORQALI BOSH HARFNI ANIQLASH
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'behi', 'banan', 'gilos']
# b_harf_a = list(filter(lambda meva: meva.startswith('a'), mevalar))
# b_harf_b = list(filter(lambda meva: meva.startswith('b'), mevalar))
# print(mevalar)
# print(b_harf_a)
# print(b_harf_b)
# =============================================================================

# =============================================================================
# # LAMBDA & FILTER
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'behi', 'banan', 'gilos']
# mevalar2 = list(filter(lambda meva: len(meva) < 5, mevalar))
# print(mevalar)
# print(mevalar2)
# =============================================================================

# =============================================================================
# # BOSH VA OXIRGI HARFLARNI TOPISH
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'behi', 'banan', 'gilos']
# a_r = list(filter(lambda meva: meva.startswith('a') and meva.endswith('r'), mevalar))
# print(mevalar)
# print(a_r)
# =============================================================================

# =============================================================================
# # FILTER / TUB SONLARNI ANIQLASH
# def tubmi(x):
#     if x % 2 == 0 or x < 2:
#         return False
#     if x == 2 or x == 3:
#         return True
#     for i in range(3, x, 2):
#         if x % i == 0:
#             return False
#     return True
# 
# tub_sonlar = list(filter(tubmi, range(100)))
# print(tub_sonlar)
# =============================================================================

# =============================================================================
# # FILTER & ODDIY FUNKSIYA
# def boshHarf(element, harf='a'):
#     """Matnning bosh harfini aniqlab True/False qiymat qaytaruvchi funksiya"""
#     return element.startswith(harf)
# 
# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'behi', 'banan', 'gilos']
# mevalar_a = list(filter(boshHarf, mevalar))
# 
# print(mevalar)
# print(mevalar_a)
# =============================================================================

































