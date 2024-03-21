# -*- coding: utf-8 -*-
"""
46-video
38-03-dars. PYTHON STANDART KUTUBXONASI
            AMALIYOT
Created on Wed Mar 20 17:41:59 2024

@author: Asadbek (devusta)
"""

import datetime as dt
import re

# =============================================================================
# # 1
# now = dt.datetime.now()
# today = now.date()
# 
# # Bugundan boshlab ikki hafta farq bilan
# # 10 ta sanani ekranga chiqarish
# next_weeks = {}
# n = 1
# for i in range(0, 20, 2):
#     difference = dt.timedelta(weeks=i)
#     next_weeks[n] = today + difference
#     print(next_weeks[n])
#     n += 1
#     
# print(next_weeks)
# =============================================================================

# =============================================================================
# # 2
# today = dt.date.today()
# 
# ramazon_hayit = dt.date(2024, 4, 10)
# qurbon_hayit = dt.date(2024, 6, 23)
# 
# print(f"Ramazon hayitigacha {(ramazon_hayit - today).days} "
#       "kun qoldi.")
# print(f"Qurbon hayitigacha {(qurbon_hayit - today).days} "
#       "kun qoldi.")
# =============================================================================

# =============================================================================
# # 3
# def get_time(year, month, day):
#     """Hozirdan berilgan sanagacha necha yil, oy va kun ekanligini qaytaruvchi funksiya"""
#     now = dt.date.today()
#     birthday = dt.date(year, month, day)
#     difference = now - birthday
#     years = difference.days // 365
#     months = (difference.days % 365) // 30
#     days = (difference.days % 365) % 30
#     return f"{years} yil, {months} oy va {days} kun"
# 
# print(f"Tug'ilganimdan beri {get_time(1999, 9, 23)} vaqt o'tdi.")
# =============================================================================

# =============================================================================
# # 4
# template = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# 
# while True:
#     phone = input("Telefon raqamini kiriting: ")
#     if re.match(template, phone):
#         print("Telefon raqam tasdiqlandi.")
#         break
#     else:
#         print("Raqam tasdiqdan o'tmadi. Qayta kiriting!")
# =============================================================================
 
# =============================================================================
# # 5
# def get_url(text):
#     """Berilgan matndan veb sahifani ajratib oluvchi funksiya"""
#     template = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
#     url = re.findall(template, text)
#     return url
# 
# text = """Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
#        Berilgan matndan veb sahifa https://www.facebook.com/ manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna"""
# 
# print(get_url(text))
# =============================================================================
                   



























