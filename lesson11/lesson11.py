# -*- coding: utf-8 -*-
"""
14-video
11-dars. IF - ELIF - ELSE

Created on Sun Feb 11 13:11:52 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # elif
# # or
# # and
# =============================================================================

# =============================================================================
# # IF - ELIF - ELSE
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4:
#     print("Siz uchun kirish bepul.")
# elif yosh <= 12:
#     print("Siz uchun kirish 5000 so'm.")    
# elif yosh <= 18:
#     print("Siz uchun kirish 7000 so'm.")
# else:
#     print("Siz uchun kirish 10000 so'm.")
# =============================================================================
    
# =============================================================================
# # IF - ELIF - ELSE
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# elif yosh <= 18:
#     narx = 7000
# else:
#     narx = 10000
# 
# print(f"Siz uchun kirish {narx} so'm.")
# =============================================================================

# =============================================================================
# # OR OPERATORI
# kun = input("Bugun qaysi kun? ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")
# =============================================================================

# =============================================================================
# # IN OPERATORI
# cars = ['bmw', 'volvo', 'kia', 'gm', 'hyundai', 'nissan']
# 
# for car in cars:
#     if car == 'bmw' or car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
# =============================================================================

# =============================================================================
# # AND OPERATORI
# hafta_kuni = input("Bugun qaysi hafta kuni? ")
# havo_harorati = float(input("Havo harorati qanday? "))
# 
# if hafta_kuni.lower() == 'shanba' and havo_harorati >= 30:
#     print("Cho'milgani boramiz.")
# elif hafta_kuni.lower() == 'yakshanba' and havo_harorati >= 30:
#     print("Cho'milgani boramiz.")
# elif hafta_kuni.lower() == 'shanba' and havo_harorati < 30:
#     print("Uyda dam olamiz.")
# elif hafta_kuni.lower() == 'yakshanba' and havo_harorati < 30:
#     print("Uyda dam olamiz.")
# else:
#     print("Belgilangan ishlarni qilamiz.")
# =============================================================================

# =============================================================================
# # OR & AND OPERATORI
# hafta_kuni = input("Bugun qaysi hafta kuni? ")
# havo_harorati = float(input("Havo harorati qanday? "))
# if (hafta_kuni.lower() == 'shanba' or hafta_kuni.lower() == 'yakshanba') and havo_harorati >= 30:
#     print("Cho'milgani boramiz.")
# elif (hafta_kuni.lower() == 'shanba' or hafta_kuni.lower() == 'yakshanba') and havo_harorati < 30:
#     print("Uyda dam olamiz.")
# else:
#     print("Belgilangan ishlarni qilmiz.")
# =============================================================================


# =============================================================================
# # BOOLEAN - TRUE, FALSE (Mantiqiy operatorlar)
# # o'zgaruvchi boolean qiymat berishda TRUE va FALSE qiymatlarini o'rniga 1 va 0 
# # foydalanishimiz ham mumkin.
# narx = 15000
# choy = True
# salat = False
# 
# if choy and salat:
#     narx = narx + 5000
# elif choy or salat:
#     narx = narx + 2500
# 
# print(f"Jami {narx} so'm.")
# =============================================================================

# =============================================================================
# # SEVERAL ONLY IF 
# # Agar biz berilgan barcha shartlarni tekshirishni xohlasak if-elif-else emas
# # faqatgina bir nechta if lardan foydalanishimiz kerak
# narx = 15000
# choy = False # 0
# non = True # 1
# salat = True # 1
# sharbat = True # 1
# assorti = False # 0
# 
# if choy:
#     print("Mijoz choy oldi.")
#     narx = narx + 1000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx + 1000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx + 1000
# if sharbat:
#     print("Mijoz sharbat oldi.")
#     narx = narx + 1000    
# if assorti:
#     print("Mijoz assorti oldi.")
#     narx = narx + 1000
#     
# print(f"Jami narx {narx} so'm.")
# =============================================================================
    
# =============================================================================
# # IN OPERATORI
# menu = ['osh', 'shashlik', 'somsa', 'lagmon', 'manti']
# ovqat = input("Nima ovqat buyurtma qilasiz?\n>>>")
# 
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Bizda bunday ovqat mavjud emas.")
# =============================================================================
        
# =============================================================================
# # NOT IN OPERATORI
# menu = ['osh', 'shashlik', 'somsa', 'lagmon', 'manti']
# yangi_ovqat = input("Yangi ovqat nomini kiriting: ")
# 
# if yangi_ovqat not in menu:
#     print("Bu ovqatni menuga qo'shish kerak!")
# else:
#     print("Bu ovqat menuda oldindan bor.")
# =============================================================================

# =============================================================================
# # IN OPERATORI
# menu = ['osh', 'shashlik', 'somsa', 'lagmon', 'manti']
# buyurtmalar = ['shashlik', 'somsa', 'norin']
# 
# 
# for ovqat in buyurtmalar:
#     if ovqat in menu:
#         print(f"Menuda {ovqat} mavjud.")
#     else:
#         print(f"Menuda {ovqat} mavjud emas.")
# =============================================================================

# =============================================================================
# # PROGRAM
# menu = ['osh', 'shashlik', 'somsa', 'lagmon', 'manti']
# buyurtmalar = ['shashlik', 'somsa', 'norin']
# mavjud_ovqatlar = []
# mavjudmas_ovqatlar = []
# 
# for ovqat in buyurtmalar:
#     if ovqat in menu:
#         mavjud_ovqatlar.append(ovqat)
#     else:
#         mavjudmas_ovqatlar.append(ovqat)
#   
# if not buyurtmalar:
#     print("Buyurtmangiz bo'sh.")
# elif buyurtmalar and len(buyurtmalar) == len(mavjud_ovqatlar):
#     print("Buyurtmadagi barcha ovqat mavjud.")
# 
# elif mavjud_ovqatlar:
#     print(f"Siz bergan buyurtmadan {len(mavjud_ovqatlar)} ta ovqat mavjud. Ular:")
#     for ovqat in mavjud_ovqatlar:
#         print(ovqat.title())
# 
# if mavjudmas_ovqatlar:
#     print(f"\nSiz bergan buyurtmadan {len(mavjudmas_ovqatlar)} ta ovqat mavjud emas. Ular:")
#     for ovqat in mavjudmas_ovqatlar:
#         print(ovqat.title())
# =============================================================================
    
    





















