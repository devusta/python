# -*- coding: utf-8 -*-
"""
21-video
18-dars. WHILE VA RO'YXATLAR
Created on Tue Feb 13 23:44:21 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# LIST WITH WHILE
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1
# while True:
#     savol = f"\n{n}-do'stingizni ismini kiriting: "
#     ism = input(savol).lower()
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shashizmi? (ha / yo'q): ").lower()
#     n += 1
#     if takrorlash != 'ha':
#         break
#     
# print("\nDo'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
# =============================================================================

# =============================================================================
# DICTIONARY WITH WHILE
# print("Do'stlaringiz va ularning yoshi haqida ro'yxat tuzamiz.")
# dostlar = {}
# n = 1
# ishora = True
# while ishora:
#     ism = input(f"\n{n}-do'stingizning ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#     n += 1
#     javob = input("Yana ma'lumot qo'shasizmi? (ha / yo'q): ") 
#     if javob == "ha":
#         ishora = True
#     elif javob == "yo'q":
#         ishora = False
#     else:
#         javob = input("Iltimos 'ha' yoki 'yo'q' deb javob bering!: ")
#         if javob == "yo'q":
#             ishora = False
#             
# for ism, yosh in dostlar.items():
#     print(f"\n{ism.title()} {yosh} yoshda.")
# =============================================================================
    
# =============================================================================
# #
# cars = ['nexia', 'lacetti', 'malibu', 'spark', 'nexia', 'captiva', 'nexia']                           
# car = 'nexia'
# while car in cars:
#     cars.remove(car)
#     
# print(cars)
# =============================================================================

# =============================================================================
# PROGRAM
# talabalar = []
# print("\nGuruhdagi talabalar va ularning baholari ro'yxatini tuzamiz.")
# talabalar_soni = int(input("\nGuruhdagi talabalar sonini kiriting: "))
# for n in range(talabalar_soni):
#     talaba_ismi = input(f"\n{n+1}-talabaning ismini kiriting: ")
#     talabalar.append(talaba_ismi)
#  
# print("\nGuruhdagi talabalar:")
# for n in range(len(talabalar)):    
#     print(f"{n+1}. {talabalar[n].title()}")
#     
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"\n{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = int(baho)
# 
# print("\nBaholangan talabalar ro'yxati:")
# n = 1
# for ism, baho in baholangan_talabalar.items():
#     print(f"{n}. {ism.title()}ning bahosi {baho} ball.")
# =============================================================================
    
# =============================================================================
# PROGRAM / MIJOZDAN BUYURTMA QABUL QILIB OLUVCHI DASTUR
# def mahsulotChiqar(list_name):
#     """LISTDAGI ELEMENTLARNI EKRANGA CHIQARUVCHI FUNKSIYA"""
#     if list_name:
#         print(f"\nSiz kiritgan {len(list_name)} ta mahsulot:")
#         a = 1
#         for n in list_name:
#             print(f"{a}. {n.title()}")
#             a += 1
#             
# mahsulotlar = {'un':50000, 'olma':5000, 'sabzi':3000, 'kartoshka':4000, "yog'":23000, 'karam':1000, 'uzum':4500}
# buyurtmalar = []
# 
# print("Kerakli mahsulotlar uchun buyurtma berishingiz mumkin.")
# n = 1
# while True:
#     buyurtma = input(f"\n{n}-mahsulot nomini kiriting!\n"
#                      "Yoki tugatish uchun 'exit' deb yozing: ").lower()
#     if buyurtma == 'exit':
#         break
#     # if buyurtma == '' or buyurtma == ' ' or buyurtma == '  ' or buyurtma == '   ':
#     if not buyurtma:
#         print("Iltimos, biror mahsulot kiriting!")
#         chiqish = input("Yoki tugatish uchun 'exit' deb yozing: ").lower()
#         if chiqish == 'exit':
#             break
#         else:
#             continue
#     if buyurtma in buyurtmalar:
#         print(f"\n{buyurtma.title()} mahsuloti {buyurtmalar.index(buyurtma)+1}-bo'lib kiritilgan.")
#         mahsulotChiqar(buyurtmalar)
#         continue
#     buyurtmalar.append(buyurtma)
#     mahsulotChiqar(buyurtmalar)
#     n += 1
#     javob = input("\nYana mahsulot kiritasizmi? (ha / yo'q): ").lower()
#     if javob == "ha":
#         continue
#     elif javob == "yo'q": 
#         break
#     else:
#         print("\nIltimos, 'ha' yoki 'yo\'q deb javob bering! ")
#         javob = input("Yana mahsulot kiritasizmi? (ha / yo'q): ").lower()
#         if javob == "yo'q": 
#             break
#     
# mahsulotChiqar(buyurtmalar) # FUNCTION
#     
# mavjud = []
# mavjud_emas = []
# for n in buyurtmalar:
#     if n in mahsulotlar:
#         mavjud.append(n)
#     else:
#         mavjud_emas.append(n)
#         
# if len(mavjud) == 1 and len(mavjud_emas) == 0:
#     print(f"\nSiz kiritgan {mavjud[0].title()} mahsuloti mavjud:")    
#     print(f"1. {mavjud[0].title()} {mahsulotlar[mavjud[0]]} so'm.")
# elif len(mavjud) > 1 and len(mavjud) == len(buyurtmalar):
#     print(f"\nSiz kiritgan {len(buyurtmalar)} ta mahsulotning barchasi mavjud:")
#     a = 1
#     for n in mavjud:    
#         print(f"{a}. {n.title()} {mahsulotlar[n]} so'm.")
#         a += 1
# elif len(mavjud) == 0 and len(mavjud_emas) == 1:
#     print(f"\nKechirasiz, Siz kiritgan {mavjud_emas[0].title()} mahsuloti mavjud emas.")
# elif len(mavjud) == 0 and len(mavjud_emas) > 1: 
#     print("\nKechirasiz, siz kiritgan barcha mahsulot mavjud emas!")
# elif len(mavjud) == 0 and len(mavjud_emas) == 0:
#     print("\nSiz hech qanday mahsulot kiritmadingiz. "
#           "\nFoydalanganingiz uchun RAHMAT!")
# else:
#     print(f"\nBuyurtmangizdan {len(mavjud)} ta mahsulot mavjud:")  
#     a = 1
#     for n in mavjud:
#         print(f"{a}. {n.title()} {mahsulotlar[n]} so'm.")
#         a += 1
#        
# if len(mavjud) > 0 and len(mavjud_emas) > 0:
#     print(f"\nQuyidagi {len(mavjud_emas)} ta mahsulot mavjud emas:")
#     a = 1
#     for n in mavjud_emas:
#         print(f"{a}. {n.title()}")
#         a += 1
# =============================================================================
        

    
    
    


































