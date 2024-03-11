# -*- coding: utf-8 -*-
"""
23-video
20-dars. FUNKSIYADAN QIYMAT QIYTARISH
Created on Thu Feb 15 17:54:31 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # return
# # 
# =============================================================================

# =============================================================================
# # SODDA FUNKSIYA
# def toliqIsmYasa(ism, familiya):
#     """TOLIQ ISM QAYTARUVCHI FUNKSIYA"""
#     toliq_ism = f"{ism} {familiya}"
#     print(toliq_ism)
#     
# toliqIsmYasa('olim', 'kamolov')
# =============================================================================

# =============================================================================
# # RETURN 
# def toliqIsmYasa(ism, familiya):
#     """TOLIQ ISM QAYTARUVCHI FUNKSIYA"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# 
# toliq_ism = toliqIsmYasa('olim', 'kamalov')
# print(toliq_ism)
#  
# talaba_1 = toliqIsmYasa('kamol', 'jamolov')
# talaba_2 = toliqIsmYasa('jasur', 'bahromov')
# print(f"Darsga {talaba_1.title()} kelmadi va "
#       f"{talaba_2.title()} kechikib keldi.")   
# =============================================================================

# =============================================================================
# # IXTIYORIY ARGUMENT
# def toliqIsmYasa(ism, familiya, sharif=''):
#     """TOLIQ ISM QAYTARUVCHI FUNKSIYA"""
#     if sharif:
#         toliq_ism = f"{ism} {sharif} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# 
# talaba_1 = toliqIsmYasa('olim', 'hakimov', 'jasurovich')
# talaba_2 = toliqIsmYasa('javlon', 'mirzayev')
# print(f"{talaba_1.title()} birinchi kurs.\n"
#       f"{talaba_2.title()} ikkinchi kurs.")
# =============================================================================

# =============================================================================
# # FUNKSIYADAN LUG'AT VA BOSHQA MA'LUMOTLARNI QAYTARISH
# def avtoInfo(brand, model, rang, karobka, yili, narx=None):
#     avto = {
#         'brand':brand,
#         'model':model,
#         'rang':rang,
#         'karobka':karobka,
#         'yili':yili,
#         'narx':narx
#         }
#     return avto
# 
# avto1 = avtoInfo('GM', 'Malibu', 'Qora', 'Avtomat', 2023)
# avto2 = avtoInfo('Kia', 'Karnival', 'Oq', 'Avtomat', 2014, 40000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi avtomashinalar:')
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}, narxi {narx}.")
# =============================================================================
        
# =============================================================================
# # RANGE FUNCTION WITHOUT STEP
# def oraliq(min, max):
#     """MA'LUM ORALIQDAGI SONLARDAN LIST YASOVCHI FUNKSIYA"""
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1 
#     return sonlar
# 
# print(oraliq(0, 10))
# range()
# =============================================================================

# =============================================================================
# # RANGE FUNCTION WITH STEP 
# def oraliq(min, max, step=''):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         if step:
#             int(step)
#             min += step 
#         else: 
#             min += 1 
#         
#     return sonlar
# 
# print(oraliq(0, 100))
# print(oraliq(0, 100, 10))
# =============================================================================

# =============================================================================
# # PROGRAM
# # FOYDALANUVCHIDAN OLINGAN MA'LUMOTLARNI LUG'ATGA VA
# # SHU LUG'ATNI LISTGA JOYLASH
# 
# def javobOl():
#     """FOYDALANUVCHIDAN RAQAM QABUL QILUVCHI FUNKSIYA"""
#     javob = int(input("Mavjud avtomobil haqida to'liq ma'lumot uchun " 
#                   "avtomobil tartib raqamini bosing!\n"
#                   "Tugatish uchun 0 ni bosing:>>> "))
#     return javob
# 
# def rahmatAyt():
#     """DASTURNI TUGAGANDAGI SO'ZNI CHIQARUVCHI FUNKSIYA"""
#     print("\nFoydalanganingiz uchun RAHMAT!")
#     
#  
# def avtoInfo(kompaniya, model, rang, karobka, yil, narx=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model, 
#         'rang': rang,
#         'karobka': karobka,
#         'yil': yil,
#         'narx': narx
#         }
#     return avto
# 
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz!")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:")
#     kompaniya = input("\nIshlab chiqaruvchi: ")
#     model = input("\nModeli: ")
#     rang = input("\nRangi: ")
#     karobka = input("\nKarobkasi: ")
#     yili = input("\nIshlab chiqarilgan yili: ")
#     narx = input("\nNarxi: ")
#     
#     if narx:
#         narx = narx
#     else:
#         narx = "Noma'lum"
#     avtolar.append(avtoInfo(kompaniya, model, rang, karobka, yili, narx))
#     
#     javob = input("Yana avtomobil qo'shasizmi? (yes / no): ")
#     if javob == 'no':
#         break
#     
# print(f"\nSalonimizdagi mavjud {len(avtolar)} ta avtomobil:")
# n = 1
# for avto in avtolar:
#     print(f"\n{n}. {avto['model'].title()}")
#     n += 1 
#     
# javob = int(input("\nMavjud avtomobil haqida to'liq ma'lumot uchun " 
#               "avtomobil tartib raqamini bosing!\n"
#               "Tugatish uchun 0 ni bosing:>>> "))
# 
# if javob == 0:
#     rahmatAyt()
# elif javob in range(1, len(avtolar)+1):
#     while True:
#         for key, value in avtolar[javob-1].items():
#             print(f"\n{key.title()}: {value.title()}")
#         
#         javob = int(input("\nMavjud avtomobil haqida to'liq ma'lumot uchun " 
#                       "avtomobil tartib raqamini bosing!\n"
#                       "Tugatish uchun 0 ni bosing:>>> "))
#                       
#         if javob == 0:
#             rahmatAyt()
#             break
#         elif javob in range(1, len(avtolar)+1):
#             continue
#         else:
#             print("\nKechirasiz, siz kiritgan tartib raqam mavjud emas!")
#             rahmatAyt()
#             break
# else:
#     print("\nKechirasiz, siz kiritgan tartib raqam mavjud emas!")
#     rahmatAyt()
# =============================================================================
    












