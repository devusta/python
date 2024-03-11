# -*- coding: utf-8 -*-
"""
25-video
22-dars. *ARGS & *KWARGS / MOSLASHUVCHAN FUNKSIYALAR
Created on Sat Feb 17 07:46:12 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # *args - infinite arguments
# # **args - moslashuvchan argumentlar kalit so'zlar bilan birga kiritilganda
# # sum() - yig'indini hisoblash
# =============================================================================

# =============================================================================
# # MOSLASHUVCHAN ARGUMENTLI FUNKSIYA
# def summa(*args):
#     """Kiritilgan sonlarni yig'indisini hisoblaydigan funksiya"""
#     total = 0
#     for number in args:
#         total += number
#     return total
# 
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# =============================================================================
    
# =============================================================================
# # MOSLASHUVCHAN ARGUMENTLI FUNKSIYA
# def summa(*sonlar):
#     """Kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     return sum(sonlar)
# 
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# 
# # STANDART VA MOSLASHUVCHAN ARGUMENTLI FUNKSIYA
# def summa(x, y, *sonlar):
#     """Kiritilgan sonlarni yig'indisini hisoblovchi funksiya"""
#     return x + y + sum(sonlar)
# 
# print(summa(1, 2))
# print(summa(1, 2, 3, 4, 5))
# print(summa(4, 5, 6, 7))
# =============================================================================
    
# =============================================================================
# # **ARGS / KALIT SO'ZLI ARGUMENTLAR
# def avtoInfo(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at shaklida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
# 
# avto1 = avtoInfo("GM", "malibu", rang='qora', yil=2018)
# avto2 = avtoInfo("KIA", "K8", rang='oq', yil=2024, korobka='avtomat')
# 
# print(avto1)
# print(avto2)
# =============================================================================

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

