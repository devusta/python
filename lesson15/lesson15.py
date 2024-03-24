# -*- coding: utf-8 -*-
"""
18-video
15-dars. DICTIONARY USTIDA AMALLAR

Created on Mon Feb 12 13:21:30 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # items() - lug'at elementlari
# # keys() - lug'at kalitlari
# # values() - lug'at qiymatlari
# # set - elementlari faqat bir marta takrorlanadigan ma'lumot turi
# =============================================================================

# =============================================================================
# talaba_1 = {'ism':'Javohir', 'familiya':'Shamsiyev', 'yosh':23, 'kurs':4}
# 
# print(talaba_1.items())
# 
# for key, value in talaba_1.items():
#     print(f"{key.title()}: {value}")
# 
# for key, value in talaba_1.items():
#     print(f"Kalit: {key.title()}")
#     print(f"Qiymat: {value}\n")
# =============================================================================

# =============================================================================
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'iphone 11',
#     'shamshod':'iphone 12',
#     'jamshid':'iphone 13',
#     'kamol':'iphone 14',
#     'mirolim':'iphone 15'
#     }
# 
# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telefoni {value}.")
# =============================================================================
    
# =============================================================================
# fruits = {'olma':2000, 'anor':2300, 'uzum':4000, 'behi':3400, 'gilos':4000}
# 
# # print(fruits.keys())
# 
# # for fruit in fruits.keys():
# #     print(fruit.title())
# 
# # for fruit in fruits:
# #     print(fruit.title())
# =============================================================================

# =============================================================================
# # PROGRAM 
# fruits = {'olma':2000, 'anor':2300, 'uzum':4000, 'behi':3400, 'gilos':4000}
# 
# bozorlik = ['olma', 'behi', 'non', 'anjir', 'uzum', 'xolva']
# print("Bizda mavjud mahsulotlar:")
# for product in bozorlik:
#     if product in fruits:
#         print(f"{product.title()} {fruits[product]} so'm.")
#     # else:
#     #     print(f"{product.title()} mahsuloti bizda mavjud emas.")
# print("\nBizda mavjud bo'lmagan mahsulotlar:")
# for product in bozorlik:
#     if product not in fruits:
#         print(product.title())
# =============================================================================

# =============================================================================
# # SORTED() FUNCTION WITH DICTIONARY
# fruits = {'olma':2000, 'anor':2300, 'uzum':4000, 'behi':3400, 'gilos':4000}
# print(sorted(fruits))
# 
# for fruit in sorted(fruits):
#     print(fruit)
# =============================================================================

# =============================================================================
# # DICTIONARYNING VALUES() METODI / FAQAT QIYMATNI OLISH
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'iphone 11',
#     'shamshod':'iphone 12',
#     'jamshid':'iphone 13',
#     'kamol':'iphone 14',
#     'mirolim':'iphone 15'
#     }
# print(telefonlar.values())
# 
# for tel in telefonlar.values():
#     print(tel)
# =============================================================================

# =============================================================================
# # SET() FUNKSIYASI / TAKRORLANISHNI OLDINI OLISH
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'iphone x',
#     'shamshod':'iphone 12',
#     'jamshid':'iphone 13',
#     'kamol':'iphone x',
#     'mirolim':'iphone 15',
#     'komil':'iphone 13',
#     'jasur':'iphone 12'
#     }
# print("Foydalanuvchilar quyidagi telefonlardan foydalanishadi.")
# for tel in set(telefonlar.values()):
#     print(tel)
# =============================================================================

# =============================================================================
# # SET MA'LUMOT TURI / SETDAGI MA'LUMOTLAR FAQAT BIR MARTA TAKRORLANADI
# toys = {'car', 'bear', 'horse', 'car', 'horse', 'lego', 'lego'}
# print(type(toys))
# print(toys)
# =============================================================================


































