# -*- coding: utf-8 -*-
"""
20-video
17-dars. INPUT() VA WHILE
Created on Tue Feb 13 16:42:23 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # int() - obyektni int turiga o'tkazish
# # str() - obyektni string turiga o'tkazish
# # float() - obyektni o'nlik son ko'rinishiga o'tkazish
# # boolean - ma'lumot turi
# # while loop 
# # break 
# # continue
# =============================================================================

# =============================================================================
# # INPUT()
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}, yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)
# =============================================================================

# =============================================================================
# ism_1 = input("Ismingizni kiriting: ").lower()
# savol_1 = f"Salom {ism_1.title()}, yoshingiz nechida? "
# yosh_1 = int(input(savol_1))
# height_1 = float(input("Bo'yingiz necha metr? "))
# =============================================================================

# =============================================================================
# # WHILE 
# son = 1
# while son <= 5:
#     print(son, end = ', ')
#     son += 1 # son = son + 1
# print("Dastur tugadi.")
# =============================================================================

# =============================================================================
# # WHILE and INPUT()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol).lower()
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi.")
# =============================================================================

# =============================================================================
# # ISHORA
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol).lower()
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi.")
# =============================================================================

# =============================================================================
# # BREAK IN WHILE
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# 
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi.")
# =============================================================================
    
# =============================================================================
# # BREAK IN FOR
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")
# =============================================================================

# =============================================================================
# # CONTINUE IN FOR
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")
# =============================================================================

# =============================================================================
# # CONTINUE IN WHILE
# son = 0
# while son < 10:
#     son += 1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)
# =============================================================================
 



























