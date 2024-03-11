# -*- coding: utf-8 -*-
"""
41-video
33-02-dars. FILES / PICKLE
Created on Sat Mar  2 18:15:36 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# # ✅NEW UNDERSTANDINGS:
# # pickle - python xos bo'gan ma'lumotlar uchun fayllar moduli
# # 'wb' - write binary / ikkilik sanoq sistemasida yozish
# # dump - pickle faylga ma'lumot qo'shish(saqlash)
# # 'rb' - read binary / ikkilik sanoq sistemasini o'qish
# # load - pickle fayldagi ma'lumotni o'qish(chaqirish)
# =============================================================================

# =============================================================================
# # Modul pickle
# import pickle  
# 
# student1 = {'name': 'hasan', 'lastname': 'husanov', 'birthyear': 2003, 'studyyear': 3}
# student2 = {'name': 'olim', 'lastname': 'valiyev', 'birhtyear': 2004, 'studyyear': 2}
# =============================================================================

# =============================================================================
# # Writing to a pickle file with 'wb'
# with open('info.pkl', 'wb') as file:
#     pickle.dump(student1, file) # dump metodi ma'lumotlarni ketma-ket joylaydi
#     pickle.dump(student2, file)
# =============================================================================

# =============================================================================
# # Writing over to a pickle file that already exists with 'wb'
# with open('info.pkl', 'wb') as file:
#     pickle.dump('olma', file)
# =============================================================================

# =============================================================================
# # Reading a pickle file with 'rb'
# with open('info.pkl', 'rb') as file:
#     talaba1 = pickle.load(file) # pickle faylda ma'lumotlarni chaqirishda xato 
#                                 # bo'lmasligi uchun bitta faylga faqat bitta
#                                 # obyekt saqlash tavsiya etiladi
#     
# print(talaba1)
# =============================================================================





































