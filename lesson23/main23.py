# -*- coding: utf-8 -*-
"""
26-VIDEO
23-DARS. MODULLAR / MAIN FILE
Created on Sun Feb 18 00:00:49 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # modul
# # from
# # import
# # as
# # math
# # random
# # randint()
# # choice()
# # shuffle()
# # import *
# =============================================================================

# =============================================================================
# # MODULDA MUROJAAT QILISH VA UNDAGI FUNKSIYALARNI CHAQIRISH
# import avto_info_mod
# 
# avto1 = avto_info_mod.avtoInfo('GM', 'Malibu', 'qora', 'avtomat', 2020, 30000)
# avto_info_mod.infoPrint(avto1)
# =============================================================================

# =============================================================================
# # MODUL NOMINI QISQA SHAKLGA KELTIRIB OLISH
# import avto_info_mod as aim
# 
# avto1 = aim.avtoInfo('GM', 'Malibu', 'qora', 'avtomat', 2020, 28000)
# aim.infoPrint(avto1)
# =============================================================================

# =============================================================================
# # MODULDAGI KERAKLI FUNKSIYALARNI JORIY FAYLGA KO'CHIRIB OLISH
# # Bu usul orqali modul nomiga qayta-qayta murojaat qilish oldi olinadi
# from avto_info_mod import avtoInfo, infoPrint
# 
# avto1 = avtoInfo('Gm', 'Malibu', 'qora', 'avtomat', 2023, 32000)
# infoPrint(avto1)
# =============================================================================

# =============================================================================
# # MODULDAGI KERAKLI FUNKSIYALARNI CHAQIRIB OLISHDA ULARNING NOMINI
# # QISQA SHAKLGA KELTIRIB OLISH 
# from avto_info_mod import avtoInfo as ainfo, infoPrint as iprint
# 
# avto1 = ainfo('GM', 'Malibu', 'qora', 'avtomat', 2022, 31000)
# iprint(avto1)
# =============================================================================

# =============================================================================
# # MODULDAGI BARCHA FUKSIYA VA O'ZGARUVCHILARNI CHAQIRIB OLISH
# # !! BU USUL TAVSIYA ETILMAYDI !!!
# from avto_info_mod import *
#  
# avto1 = avtoInfo('GM', 'Malibu', 'qora', 'avtomat', 2021, 29000)
# infoPrint(avto1)
# =============================================================================

# PYTHONDA MAVJUD BO'LGAN MODULLAR:
# =============================================================================
# # MATH MODULI
# import math
# 
# x = 400
# print(math.sqrt(x))
# print(math.pow(5, 3))
# print(math.pi)
# print(math.log2(8))
# print(math.log10(100))
# =============================================================================

# =============================================================================
# # RANDOM MODULI
# import random as rm
# 
# # RANDINT() - ma'lum oraliqadagi tasodifiy sonni qaytaradi
# son = rm.randint(0, 100)
# print(son)
# 
# # CHOICE() - ro'yxatdan tasodifiy elementni qaytaradi
# ismlar = ['olim', 'kamol', 'bahrom', 'ilhom', 'hoshim', 'jasur']
# ism = rm.choice(ismlar)
# print(ism)
# print(rm.choice(ism))
# 
# x = list(range(0, 51, 5))
# print(x)
# print(rm.choice(x))
#  
# # SHUFFLE() - ma'lum elementlar tartibini o'zgartirib qaytaradi
# n = list(range(11))
# print(n)
# rm.shuffle(n)
# print(n)
# =============================================================================






























