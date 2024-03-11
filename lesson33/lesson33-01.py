# -*- coding: utf-8 -*-
"""
41-video
33-01-dars. FILES / FAYLLAR BILAN ISHLASH
Created on Sat Mar  2 15:21:51 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# # ✅NEW UNDERSTANDINGS:
# # open() - faylni ochish, 
# # close() - faylni yopish 
# # read() - faylni o'qish
# # write() - yozish metodi
# # rstrip() - o'ng tarafdagi bo'shliqni olib tashlash
# # line - o'zgaruvchi qatori
# # readlines() - qatorlarni alohida o'qish
# # replace() - bir elementni boshqa elementga almashtirish 
# # 'r' - to read
# # 'w' - to write / faylning barcha ma'lumotlari o'chirib ustidan yozish
# # 'a' - to append / fayl ma'lumotlariga yangi ma'lumot qo'shish
# =============================================================================

# =============================================================================
# # Fayllar bilan ishlashdagi TAVSIYA ETILMAGAN usullar
# file = open('pi.txt') # Faylni ochish va uni 'file' o'zgaruvchiga yuklash
# PI = file.read() # Fayldagi ma'lumotni o'qish va 'PI' o'zgaruvchiga yuklash
# print(PI)
# file.close() # Faylni yopish
# =============================================================================

# =============================================================================
# # Fayllar bilan ishlashdagi TAVSIYA ETILGAN usullar
# =============================================================================
# =============================================================================
# with open('pi.txt') as file: # Faylni ochish va uni 'file' o'zgaruvchisiga yuklash
#     PI = file.read() # Fayldagi ma'lumotni o'qish va 'PI' o'zgarubchisiga yuklash
#     
# print(PI)
# 
# PI = PI.rstrip() # O'zgaruvchi ma'lumotining o'ng tarafidagi bo'shliqni olib tashlash
# PI = PI.replace('\n', '') # Ma'lumotdagi qator tashlash belgisi('\n')ni qo'shilish('')
#                           # belgisiga almashtirish
# PI = float(PI) # Ma'lumot turini o'zgartirish
# print(PI)
# =============================================================================

# =============================================================================
# filename = 'data/students.txt'     # Faylni chaqirish
# with open(filename) as file:       # Faylni ochish
#     for line in file:              # O'zgaruvchidagi har bir ma'lumot qatorini
#         print(line)                # ekranga chiqarish
# =============================================================================

# =============================================================================
# filename = 'data/students.txt'
# with open(filename) as file:
#     students = file.readlines() # O'zgaruvchidagi har bir qatorni alohida qilib
#                                 # ro'yxatga joylash
#                                 
# print(students)                        
# 
# # method 1
# # students = [student.rstrip() for student in students]
# 
# # method 2
# students = [student.replace('\n', '') for student in students]
# print(students)
# =============================================================================

# =============================================================================
# # Writing to a file with 'w' / to write
# filename = 'new_file.txt' # yangi fayl yaratish
# name = "Tohir Murodov"
# birthyear = 1998
# with open(filename, 'w') as file:
#     file.write(name)
#     file.write(str(birthyear))
# =============================================================================
    
# =============================================================================
# # Writing over to a file that already exists with 'w' / to write over
# filename = 'new_file.txt' # mavjud faylni chaqirish
# name = "Kamol Jamolov"
# birthyear = 1995
# with open(filename, 'w') as file:
#     file.write(name + '\n')
#     file.write(str(birthyear) + '\n')
# =============================================================================

# =============================================================================
# # Writing to a file with 'w' / to write
# filename = 'data/new_file.txt' # yangi fayl yaratish
# name = "Tohir Murodov"
# birthyear = 1998
# with open(filename, 'w') as file:
#     file.write(name + '\n')
#     file.write(str(birthyear) + '\n')
# =============================================================================

# =============================================================================
# # Writing to a file with 'a' / to append
# filename = 'new_file.txt'
# with open(filename, 'a') as file:
#     file.write('Alijon Hoshimov\n')
#     file.write('2000')
# =============================================================================


















































