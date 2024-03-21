# -*- coding: utf-8 -*-
"""
46-video
38-03-dars. PYTHON STANDART KUTUBXONASI
            PPRINT, RegEx(Regular Expressions) MODULLARI
Created on Wed Mar 20 14:22:07 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # pprint - obyektlarni ekranga chiroyli qilib 
#          # chiqarishda foydalananiladigan modul
# # pprint() - pprint modulidagi funksiya
# # re - RegEx modulininig qisqa nomi. Bu modul
#        # andozalar yaratishda foydalaniladi
# # re.match() - berilgan andozaga berilgan obyekt
#                # mos tushsa obyektni qaytaruvchi funksiya
# # re.findall() - emaillarni andoza yordamida ajratib olish
# =============================================================================


# 1. pprint moduli
import pprint as p

# =============================================================================
# # json fyldagi ma'lumotlarni chiroyli ko'rinishda chiqarish
# import requests
# r = requests.get('https://api.github.com')
# print(r.json()) # oddiy print bilan
# p.pprint(r.json()) # pprint funksiyasi bilan
# =============================================================================

# 2. RegEx moduli
import re

# =============================================================================
# # RegEx modulidan foydalanish
# word1 = "temir"
# word2 = "tomir"
# word3 = "tandir"
# template = "^t...r$"
# 
# print(re.match(template, word1))
# print(re.match(template, word2))
# print(re.match(template, word3))
# =============================================================================

# =============================================================================
# # Ro'yxatdan andozaga mos keluvchi elementlarni ajratib olish
# words = ['teacher', 'timer', 'tinker', 'trailer', 'tanker', 'taster', 'toner', 'tutor', 'tender', 'trimmer', 'thriller', 'trawler', 'transfer', 'tinkerer', 'tracker', 'trigger', 'tunder', 'teller', 'topper', 'tumbler', 'tear', 'tormentor', 'teaser', 'torcher', 'tweaker']
# template = "^t....r$"
# matches = []
# 
# # for word in words:
# #     if re.match(template, word):
# #         matches.append(word)
# 
# # yuqoridagi kod bir qatorda
# matches = [word for word in words if re.match(template, word)]
# print(matches)
# =============================================================================

# Emailni ajratib olish
text = """Maqolalar 2020-yil 20-martga qadar dfsdhfkjsdfksd@mail.ru pochta manziliga
       jo'natilsin. Yoki klhjh@gmail.com emiliga yuboring."""

template = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(template, text)
print(email)

# =============================================================================
# # Kuchli parolni tekshirish
# template = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# msg = """Yangi parol kiriting (parol tarkibi kamida 1 ta lotin bosh harf, 
# 1 ta kichik harf, 1 ta raqam va 1 ta maxsus belgidan iborat kamida 8 xonali bo'lishi kerak: """
# 
# while True:
#     password = input(msg)
#     if re.match(template, password):
#         print("Parol yaratildi.")
#         break
#     else:
#         print("Parol talabga javob bermadi.")
# =============================================================================
        
    












