# -*- coding: utf-8 -*-
"""
26-video
23-dars. MODULLAR / AVTO INFOLAR BO'YICHA FUNKSIYALARNI SAQLOVCHI MODUL
Created on Sat Feb 17 11:59:19 2024

@author: Asadbek (devusta)
"""

def avtoInfo(kompaniya, model, rang, karobka, yili, narx):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rang,
        'karobka': karobka,
        'yil': yili,
        'narx': narx
        }
    return avto

def avtoKirit():
    """Foydalanuvchiga avtoInfo funksiyasi yordamida bit nechta avtolar
    haqida ma'lumotlarni bitta ro'yxatda jamlab beruvchi funksiya"""
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rang = input("Rangi: ")
        karobka = input("Karobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narx = input("Narxi: ")
        
        avtolar.append(avtoInfo(kompaniya, model, rang, karobka, yili, narx))
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob == 'no':
            break
    return avtolar

def infoPrint(avtoInfo):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avtoInfo['rang'].title()} {avtoInfo['kompaniya'].upper()} "
          f"{avtoInfo['model'].upper()}, {avtoInfo['karobka']} karobka, "
          f"{avtoInfo['yil']}-yil, {avtoInfo['narx']}$")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        