# -*- coding: utf-8 -*-
"""
47-video
39-01-dars. PYTHON TASHQI KUTUBXONASI
            Googletrans MODULI
Created on Thu Mar 21 10:24:47 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # PyPi.org - eng ko'p foydalaniladigan python tashqi kutubxonasi
# # wikipedia - wikipedia ma'lumotlariga oson kirish va tahlil qilish uchun modul
# # googletrans - matnni turli tillarga tarjima qilishda foydalaniladigan modul
# # Translater - translater modulidagi tarjimon klassi
# # translate() - matnni tarjima qilish uchun metod
#                 # matndan boshqa parametr berilmasa o'z-o'zidan ingliz tiliga tarjima qiladi
# # .origin - matnni orginalini chaqirish uchun xususiyat
# # .text - obyektning matnni chaqirish uchun xususiyat
# # .src - orginal matn qaysi tilda ekanligini ko'rsatuvchi xususiyat
# # dest - tarjima qilinishi kerak bo'lgan til uchun parametr
# =============================================================================

# googletrans modulidagi Translater klassini chaqirish
from googletrans import Translator
# Translator klassidan obyekt yaratish
tarjimon = Translator()

# =============================================================================
# # O'zbekcha matnni ingliz tiliga tarjima qilish
# text_uz = "Men Python dasturlash tilida kod yozaman."
# 
# # Istalgan matnni ingliz tiliga tarjima qilish uchun translate metodini chaqiramiz
# translated_text = tarjimon.translate(text_uz)
# 
# print(translated_text.origin) # Original matn
# print(translated_text.text) # Tarjima qilingan matn
# print(translated_text.src) # Asl matn qaysi tilda
# =============================================================================

# =============================================================================
# # Matnni ingliz tilidan boshqa tilga tarjima qilish
# text_uz = "Men Python dasturlash tilida kod yozaman."
# 
# translate_ru = tarjimon.translate(text_uz, dest='ru')
# print(translate_ru.text)
# =============================================================================

# =============================================================================
# # Matnni ingliz tilidan tarjima qilish
# text_en = "Tashkent is the capital of Uzbekistan."
# translated_uz = tarjimon.translate(text_en, dest='uz')
# translated_ru = tarjimon.translate(text_en, dest='ru')
# print(translated_uz.text)
# print(translated_ru.text)
# =============================================================================

# =============================================================================
# # Sodda tarjimon dastur
# msg = "Matn kiriting: "
# while True:
#     text = input(msg)
#     if text == "1":
#         break
#     else:
#         translated_text = tarjimon.translate(text, src='uz', dest='en')
#         print(translated_text.text)
# =============================================================================
























