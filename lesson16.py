# -*- coding: utf-8 -*-
"""
19-video
16-dars. NESTING

Created on Mon Feb 12 15:11:19 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# # DICTIONARY(LUG'ATLAR)NI BIRMA-BIR YARATISH VA 
# # EKRANGA CHIQARISH
# car_0 = {
#     'model':'malibu',
#     'rang':'qizil',
#     'narx':'30000',
#     'karobka':'avto'
#     }
# 
# car_1 = {
#     'model':'lacetti',
#     'rang':'qora',
#     'narx':'20000',
#     'karobka':'mexanika'
#     }
# 
# car_2 = {
#     'model':'cobalt',
#     'rang':'kulrang',
#     'narx':'18000',
#     'karobka':'mexanika'
#     }
# 
# car = car_0
# print(f"{car['model'].title()}, "
#       f"rangi {car['rang']}, "
#       f"narxi {car['narx']}$, "
#       f"karobkasi {car['karobka']}.")
# 
# car = car_1
# print(f"{car['model'].title()}, "
#       f"rangi {car['rang']}, "
#       f"narxi {car['narx']}$, "
#       f"karobkasi {car['karobka']}.")
# 
# car = car_2
# print(f"{car['model'].title()}, "
#       f"rangi {car['rang']}, "
#       f"narxi {car['narx']}$, "
#       f"karobkasi {car['karobka']}.")
# =============================================================================

# =============================================================================
# # LUG'ATLARNI FOR SIKLI ORQALI EKRANGA CHIQARISH
# car_0 = {
#     'model':'malibu',
#     'rang':'qizil',
#     'narx':'30000',
#     'karobka':'avto'
#     }
# 
# car_1 = {
#     'model':'lacetti',
#     'rang':'qora',
#     'narx':'20000',
#     'karobka':'mexanika'
#     }
# 
# car_2 = {
#     'model':'cobalt',
#     'rang':'kulrang',
#     'narx':'18000',
#     'karobka':'mexanika'
#     }
# 
# cars = [car_0, car_1, car_2]
# # for car in cars:
# #     print(f"{car['model'].title()}, "
# #           f"rangi {car['rang']}, "
# #           f"narxi {car['narx']}$, "
# #           f"karobkasi {car['karobka']}.")
# 
# # print(cars[0]) # listni ichidagai lug'atga murojat qilish
# 
# print(cars[2]['rang']) # listni ichidagi lug'atning ma'lum element qiymatiga murojaat qilish
# 
# print(f"{cars[0]['model'].title()}ning rangi {cars[0]['rang']}")
# =============================================================================

# =============================================================================
# # LUG'ATLARNI FOR SIKLI YORDAMIDA OSONLIK BN YARATISH 
# # VA UNI O'ZGARTIRISH
# malibus = []
# for n in range(10):
#     new_item = {
#         'nomi':'malibu',
#         'rang':None,
#         'km':0,
#         'karobka':'avto',
#         'narx':None
#         }
#     malibus.append(new_item)
#     
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
#     
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
#     
# for malibu in malibus[6:]:
#     malibu['rang'] = 'oq'
#     
# for malibu in malibus[4:7]:
#     malibu['karobka'] = 'mexanika'
#     
# for malibu in malibus:
#     if malibu['rang'] == 'oq' or malibu['karobka'] == 'avto':
#         malibu['narx'] = 35000
#     else:
#         malibu['narx'] = 30000
# =============================================================================
     

# =============================================================================
# # PROGRAMM
# countries = []
# for n in range(3):
#     new_country = {
#         'name':None,
#         'location':None,
#         'language':None,
#         'population':None,
#         'area':None
#         }
#     countries.append(new_country)
# 
# countries_name = []
# countries_location = []
# countries_language = []
# countries_population = []
# countries_area = []
# 
# for n in range(3):
#     country_name = input(f"{n+1}-davlat nomini kiriting: ")
#     countries_name.append(country_name)
#     
#     country_location = input(f"{n+1}-davlat joylashuvini kiriting: ")
#     countries_location.append(country_location)
#     
#     country_language = input(f"{n+1}-davlat tilini kiriting: ")
#     countries_language.append(country_language)
#     
#     country_population = input(f"{n+1}-davlat aholi sonini kiriting: ")
#     countries_population.append(country_population)
#     
#     country_area = input(f"{n+1}-davlat maydonini kiriting: ")
#     countries_area.append(country_area)
#     
# for n in range(3):
#     countries[n]['name'] = countries_name[n]
#     countries[n]['location'] = countries_location[n]
#     countries[n]['language'] = countries_language[n]
#     countries[n]['population'] = countries_population[n]
#     countries[n]['area'] = countries_area[n]
# =============================================================================

# =============================================================================
# # lUG'AT ICHIDA RO'YXAT / LIST IN DICTIONARY
# dasturchilar = {
#     'ali':['python', 'php'],
#     'vali':['php', 'c++'],
#     'komil':['c#', 'java'],
#     'mirza':['js', 'c#']
#     }
# 
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} {tillar[0].upper()} va {tillar[1].upper()} "
#           "dasturlash tillarini biladi.")
# =============================================================================

# =============================================================================
# # LUG'AT ICHIDA LUG'AT / DICTIONARY IN DICTINARY
# hamkasblar = {
#     'ali':{
#         'familiya':'komilov',
#         'tyil':1995,
#         'malumot':'oliy',
#         'tillar':['c++', 'java']
#         },
#     'vali':{
#         'familiya':'hoshimov',
#         'tyil':1990,
#         'malumot':'orta',
#         'tillar':['js', 'php', 'c#']
#         },
#     'komil':{
#         'familiya':'muxtorov',
#         'tyil':1998,
#         'malumot':'oliy',
#         'tillar':['c++', 'js', 'python']
#         }
#     }
# 
# for ism, info in hamkasblar.items():
#     print(f"\n\n{ism.title()} {info['familiya'].title()} "
#           f"{info['tyil']}-yilda tug'ilgan, "
#           f"ma'lumoti {info['malumot']}. \n"
#           "Biladigan dasturlash tillari quyidagilar:", end=' ')
#     for til in info['tillar']:
#         print(til.upper(), end=', ')
# =============================================================================

# =============================================================================
# # PROGRAMM 
# davlat_soni = int(input("Ro'yxatini tuzmoqchi bo'lgan davlat sonini kiriting: "))
# print(f"\nSiz {davlat_soni} ta davlat ro'yxatini tuzishga qaror qildingiz!\n")
# 
# print("Davlat nomlarini tartib bilan kiritishni boshlang!\n")
# davlatlar_nomi = []
# for n in range(davlat_soni):
#     davlat = input(f"{n+1}-davlat nomini kiriting: ").lower()
#     davlatlar_nomi.append(davlat)
#     
# print(f"\nEndi siz kiritgan {davlat_soni} ta davlatning ma'lumotlarini kiriting!\n")
# davlatlar_info = {}
# for n in davlatlar_nomi:
#     if n == 'aqsh':
#         davlat = {
#             'poytaxt':input(f"\n{n.upper()}ning poytaxtini kiriting: "),
#             'hudud':input(f"{n.upper()}ning hududini kiriting: "),
#             'aholi':input(f"{n.upper()}ning aholi sonini kiriting: "),
#             'pul_birligi':input(f"{n.upper()}ning pul birligini kiriting: ")
#             }
#     else:
#         davlat = {
#             'poytaxt':input(f"\n{n.title()}ning poytaxtini kiriting: "),
#             'hudud':input(f"{n.title()}ning hududini kiriting: "),
#             'aholi':input(f"{n.title()}ning aholi sonini kiriting: "),
#             'pul_birligi':input(f"{n.title()}ning pul birligini kiriting: ")
#             }
#     davlatlar_info[n] = davlat
# 
# print(f"\nSiz kiritgan {davlat_soni} ta davlatning ma'lumotlari quyidagilar:\n")
# for n in davlatlar_info:
#     if n == 'aqsh':
#         print(f"\n{n.upper()}ning poytaxti {davlatlar_info[n]['poytaxt'].title()}\n"
#           f"Hududi: {davlatlar_info[n]['hudud']} kv.km\n"
#           f"Aholisi: {davlatlar_info[n]['aholi']} kishi\n"
#           f"Pul birligi: {davlatlar_info[n]['pul_birligi']}")
#     else:
#         print(f"\n{n.title()}ning poytaxti {davlatlar_info[n]['poytaxt'].title()}\n"
#               f"Hududi: {davlatlar_info[n]['hudud']} kv.km\n"
#               f"Aholisi: {davlatlar_info[n]['aholi']} kishi\n"
#               f"Pul birligi: {davlatlar_info[n]['pul_birligi']}")
# =============================================================================
    
# =============================================================================
# # PROGRAMM
# davlatlar_info = {
#     "o'zbekiston": {
#         'poytaxt': 'toshkent',
#         'hudud': '448978',
#         'aholi': '38000000',
#         'pul_birligi': "so'm"
#         },
#    'rossiya': {
#        'poytaxt': 'moskva',
#        'hudud': '17098246',
#        'aholi': '144000000',
#        'pul_birligi': 'rubl'
#        },
#    'aqsh': {
#        'poytaxt': 'vashington',
#        'hudud': '9631418',
#        'aholi': '327000000',
#        'pul_birligi': 'dollor'
#        },
#    'malayziya': {
#        'poytaxt': 'kuala-lumpur',
#        'hudud': '329750',
#        'aholi': '25000000',
#        'pul_birligi': 'rinngit'
#        }
#    }
# 
# for n in davlatlar_info:
#     if n == 'aqsh':
#         print(f"\n{n.upper()}ning poytaxti {davlatlar_info[n]['poytaxt'].title()}\n"
#           f"Hududi: {davlatlar_info[n]['hudud']} kv.km\n"
#           f"Aholisi: {davlatlar_info[n]['aholi']} kishi\n"
#           f"Pul birligi: {davlatlar_info[n]['pul_birligi']}")
#     else:
#         print(f"\n{n.title()}ning poytaxti {davlatlar_info[n]['poytaxt'].title()}\n"
#               f"Hududi: {davlatlar_info[n]['hudud']} kv.km\n"
#               f"Aholisi: {davlatlar_info[n]['aholi']} kishi\n"
#               f"Pul birligi: {davlatlar_info[n]['pul_birligi']}")
# =============================================================================

# =============================================================================
# # PROGRAMM
# davlatlar_info = {
#     "o'zbekiston": {
#         'poytaxt': 'toshkent',
#         'hudud': '448978',
#         'aholi': '38000000',
#         'pul_birligi': "so'm"
#         },
#     'rossiya': {
#         'poytaxt': 'moskva',
#         'hudud': '17098246',
#         'aholi': '144000000',
#         'pul_birligi': 'rubl'
#         },
#     'aqsh': {
#         'poytaxt': 'vashington',
#         'hudud': '9631418',
#         'aholi': '327000000',
#         'pul_birligi': 'dollor'
#         },
#     'malayziya': {
#         'poytaxt': 'kuala-lumpur',
#         'hudud': '329750',
#         'aholi': '25000000',
#         'pul_birligi': 'rinngit'
#         }
#     }
# 
# n = input("Davlat nomini kiriting: ").lower()
# 
# if n in davlatlar_info:
#     info = davlatlar_info[n]
#     print(f"\n{n.title()}ning poytaxti {davlatlar_info[n]['poytaxt'].title()}\n"
#           f"Hududi: {davlatlar_info[n]['hudud']} kv.km\n"
#           f"Aholisi: {davlatlar_info[n]['aholi']} kishi\n"
#           f"Pul birligi: {davlatlar_info[n]['pul_birligi']}")
# else:
#     print(f"Kechirasiz, {n.title()} haqida bizda ma'lumot mavjud emas.")
# =============================================================================







