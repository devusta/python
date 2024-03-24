# -*- coding: utf-8 -*-
"""
43-video
35-dars. ERRORS (XATOLAR BILAN ISHLASH)
Created on Sat Mar 16 01:46:28 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# # ✅NEW UNDERSTANDINGS:
# # exception - istisno
# # try - xatolik yuz berishi mumkin bo'lgan kod oldidan yoziladi
# # except - xatolik yuz berganda bajarilishi kerak bo'lgan kod oldidan yoziladi
# # else for exception - xatolik yuz bermasa  bajariladigan kod oldidan yoziladi
# # pass - kod qaysidir qismini shunchaki o'tkazib yuborish
# # isdigit() - obyektni raqamlardan iborat yoki yo'qligini tekshiradi
# # finally
# =============================================================================

# =============================================================================
# # try and except
# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
#     print(f"Siz {2024-age}-yilda tug'ilgansiz.")
# except:
#     print("Butun son kiritmadingiz!")
# =============================================================================

# =============================================================================
# # with else
# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
# except:
#     print("Siz butun son kiritmadingiz!")
# else:
#     print(f"Siz {2024-age}-yilda tug'ilgansiz.")
# =============================================================================

# =============================================================================
# # with Error type
# age = input("Yoshingizni kiriting: ")
# try: 
#     age = int(age)
# except ValueError: # error type
#     print("Siz butun son kiritmadindiz!")
# else:
#     print(f"Siz {2024-age} yilda tug'ilgansiz.")
# =============================================================================

# =============================================================================
# # ZeroDivisionError
# x, y = 5, 10
# try:
#     y / (x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas.")
# =============================================================================

# =============================================================================
# # IndexError
# fruits = ['olma', 'behi', 'uzum', 'nok']
# try:
#     print(fruits[4])
# except IndexError:
#     print(f"Ro'yxatda faqat {len(fruits)} ta meva bor.")
# =============================================================================
        
# =============================================================================
# # KeyError
# user = {"username": "devusta", 
#         "status": "admin",
#         "email": "admin@devusta.dev",
#         "phone": "01012345678"}
# 
# key = "address"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas.")
# =============================================================================

# =============================================================================
# # FileNotFoundError
# filename = "data.txt"
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} fayli mavjud emas")
# =============================================================================

import json
# =============================================================================
# # with many files
# files = ['student1.json', 'student.json', 'student2.json', 'student3.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             student = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} fayli mavjud emas.")
#     else:
#         print(student['name'])
# =============================================================================

# =============================================================================
# # pass
# files = ['student1.json', 'student.json', 'student2.json', 'student3.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             student = json.load(f)
#     except FileNotFoundError:
#         pass
#     else: 
#         print(student['name'])
# =============================================================================

# =============================================================================
# # more excepts
# n = input("Butun son kiriting: ")
# try: 
#     n = int(n)
#     x = 20/n
# except ValueError: # butun son kiritilmasa ishga tushadi
#     print("Butun son kiritilmadi.")
# except ZeroDivisionError: # 0 kiritilsa ishga tushadi
#     print("0 ga bo'lish mumkin emas.")
# else:
#     print(f"x = {x}")
# =============================================================================

# =============================================================================
# # try-except operatorlari oldini olib bo'lmaydigan va ko'zda tutilmagan
# # xatolar uchun yoziladi.
# # Oldini olsa bo'ladigan xatolar uchun esa boshqa choralar ko'rish kerak
# while True:
#     age = input("Yoshingizni kiriting: ")
#     if age.isdigit():
#         age = int(age)
#         break
# 
# print(f"Siz {2024-age}-yilda tug'ilgansiz.")
# =============================================================================
    























