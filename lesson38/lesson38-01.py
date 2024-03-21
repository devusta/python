# -*- coding: utf-8 -*-
"""
46-video
38-01-dars. PYTHON STANDART KUTUBXONASI /  DATETIME MODULI
Created on Tue Mar 19 04:01:06 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # docs.python.org/3/library - pythonning modullari joylashgan kutubxona
# # datetime - sana va vaqtlar bilan ishlash moduli
# # .datetime - moduldagi sana va vaqtni chiqaruvchi obyekt
# # .now() - hozirgi sana va vaqtni chaqirish
# # .date() - sanani chaqiruvchi metod
# # .time() - vaqtni chaqiruvchi metod
# # .hour - faqat soatni chaqirish
# # .minute - faqat minutni chaqirish
# # .second - faqat sekuntni chaqirish
# # .date - moduldagi sanani chiqaruvchi obyekt
# # .today() - bugungi sanani chaqiruvchi metod
# # -vaqtlarni farqini ko'rish
# # .days - obyektdan kunlarni ajratib olish
# # timedelta() - sanalarning farqini kiritish
# =============================================================================

import datetime as dt

# =============================================================================
# # datetime 
# now = dt.datetime.now()
# print(now)
# # sana
# print(now.date())
# # vaqt
# print(now.time())
# # soat
# print(now.hour)
# # minut
# print(now.minute)
# # soniya
# print(now.second)
# =============================================================================

# =============================================================================
# # date / Sanani chaqirish
# today = dt.date.today()
# print(f"Bugungi sana: {today}")
# =============================================================================

# =============================================================================
# # Sanani qo'lda kiritish
# tomorrow = dt.date(2024, 3, 20)
# print(f"Ertangi sana: {tomorrow}")
# =============================================================================

# =============================================================================
# # Vaqtni chaqirish
# now = dt.datetime.now()
# 
# time_now = now.time()
# print(f"Hozirgi vaqt: {time_now}")
# =============================================================================

# =============================================================================
# # Vaqtni qo'lda kiritish
# time_after1 = dt.time(23, 45, 32)
# time_after2 = dt.time(12, 23, 59, 999999) # milli sekunt bilan
# print(f"Keyingi vaqt: {time_after1}")
# print(f"Keyingi vaqt: {time_after2}")
# =============================================================================

# =============================================================================
# # Sanalar orasidagi farq
# today = dt.date.today()
# friday = dt.date(2024, 3, 22)
# difference = friday - today
# print(difference) # farq
# print(difference.days) # farqning faqat kuni ajratib olish
# print(f"Juma kuniga {difference.days} kun qoldi.")
# =============================================================================

# =============================================================================
# # Soatlar orasidagi farq
# now = dt.datetime.now()
# football_date = dt.datetime(2024, 3, 30, 23, 30, 00)
# difference = football_date - now
# print(difference.days) # farqning kunini ajratib olish
# print(difference.seconds) # sekuntlarni ajratib olish
# 
# # farqdagi jami sekuntlarni ajratib olish va soat, minut va soniyalarga bo'lish
# total_seconds = difference.seconds # sekuntlarni ajratib olish
# hours = total_seconds // 3600 # jami sekuntlar ichida necha soat bor
# minuts = (total_seconds % 3600) // 60 # qolgan sekuntlar ichida necha minut bor
# seconds = (total_seconds % 3600) % 60 # hammasidan qolgan sekuntlar
# 
# print(f"Futbol o'yinigacha {difference.days} kun, {hours} soat, "
#        f"{minuts} daqiqa va {seconds} soniya qoldi.")
# =============================================================================

























