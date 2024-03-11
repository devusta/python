# -*- coding: utf-8 -*-
"""
17-video
14-dars. DICTIONARY (Lug'at)

Created on Sun Feb 11 22:41:03 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # dictionary
# # get() - lug'at elementlari bilan ishlovchi maxsus metod
# =============================================================================

# =============================================================================
# # CREATE DICTIONARIES
# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
# =============================================================================

# =============================================================================
# # CREATE DICTIONARIES
# en_uz = {'apple':'olma', 'banana':'banan', 'apricot':"o'rik"}
# 
# mevalar = {'olma':1000, 'nok':2000, 'gilos':3000}
# print(f"Olmaning narxi {mevalar['olma']} so'm")
# 
# 
# talaba_0 = {'ism':'murod olimov', 'yosh':23, 't_yil':2000}
# print(f"{talaba_0['ism'].title()} {talaba_0['t_yil']}-yilda tug'ilgan,\
#   {talaba_0['yosh']} yoshda.")
# =============================================================================

# =============================================================================
# # LUG'ATGA YANGI ELEMENT QO'SHISH VA UNI O'ZGARTIRISH
# talaba_0 = {'ism':'murod olimov', 'yosh':23, 't_yil':2000}
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'
# 
# print(talaba_0)
# =============================================================================

# =============================================================================
# # BO'SH LUG'AT YARATISH VA UNGA ELEMENT QO'SHISH
# talaba_1 = {}
# talaba_1['ism'] = 'komil'
# talaba_1['yosh'] = 34
# talaba_1['kurs'] = 3
# 
# print(f"Talaba {talaba_1['ism'].title()}\
#   {talaba_1['yosh']} yoshda, {talaba_1['kurs']}-kursda o'qiydi.")
# =============================================================================

# =============================================================================
# # DEL OPERATORI - LUG'AT ELEMENTINI O'CHIRISH 
# talaba_2 = {'ism':'Jamol', 'yosh':23, 'millati':'uzbek'}
# print(talaba_2)
# del talaba_2['millati']
# print(talaba_2)
# =============================================================================

# =============================================================================
# # LUG'AT ELEMENTLARINI BIR NECHA QATORGA YOZISH
# avtolar = {
#     'mirjalol':'damas',
#     'javohir':'labo',
#     'barkamol':'equinox',
#     'abdulloh':'damas',
#     'hurshid':'porter'
#     }
# =============================================================================
    
# =============================================================================
# # GET() METODI
# mevalar = {'olma':1000, 'gilos':2000, 'olcha':3000}
# meva = mevalar.get('gilos', 'Bunday element mavjud emas.')
# meva1 = mevalar.get('nok', 'Bunday element mavjud emas.')
# print(meva)
# print(meva1)
# =============================================================================














