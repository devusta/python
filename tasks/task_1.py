# -*- coding: utf-8 -*-
"""
Python asoslari uchun vazifa
Created on Sat Mar 23 12:30:38 2024

@author: Asadbek (devusta)
"""
import random as r

# user_name() function
def user_name():
    """Foydalanuvchidan ismini so'rab, ismini teskarisiga 0, 9 oralig'ida
    tasodifiy son qo'shib natijani qaytaruvchi funksiya"""
    name = input("Ismingizni kiriting: ")
    username = name[::-1] + str(r.randint(0, 9))
    return f"Siz uchun generatsiya qilingan username: {username}"


# convert_add function
convert_add = lambda list_name: sum([int(item) for item in list_name])

# testing user_name()
print(user_name())

# testing convert_add()
print(convert_add(['1', '3', '5', '34', '4']))























