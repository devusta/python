# -*- coding: utf-8 -*-
"""
47-video
39-02-dars. PYTHON TASHQI KUTUBXONASI
            Requests MODULI
            BeautifulSoup MODULI
Created on Thu Mar 21 11:24:18 2024

@author: Asadbek (devusta)
"""
# ✅NEW UNDERSTANDINGS
# requests - internetdagi sahifalarni chaqrib olish uchun modul
# get() - moduldagi chaqirish metodi
# BeautifulSoup - obyektni ichidan faqat kerakligi elementlarni sug'urib oluvchi modul
                # odatda requests moduli bilan ishlatiladi
# prettify() - html kodlarni tartiblab beruvchi metod
# find_all() 
# class_

import requests
from pprint import pprint
import googletrans

# =============================================================================
# # requests modulidan foydalanish
# webpage = "https://kun.uz/news/main"
# request1 = requests.get(webpage)
# pprint(request1.text)
# =============================================================================

# =============================================================================
# # restcountries API
# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# request = requests.get(url)
# request_json = request.json()[0]
# print(request_json)
# =============================================================================

# =============================================================================
# # adviceslip API
# url = "https://api.adviceslip.com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# advice_id = r.json()['slip']['id']
# 
# print(f"{advice_id}. {advice}")
# 
# translator = googletrans.Translator()
# translated_text = translator.translate(advice, dest='uz')
# print(f"{advice_id}. {translated_text.text}")
# =============================================================================

from bs4 import BeautifulSoup

# =============================================================================
# # BeautifulSoup modulidan foydalanish
# webpage = "https://kun.uz/news/main"
# r = requests.get(webpage)
# # pprint(r.text)
# 
# # modul yordamida vebsahifadagi html kodlarni olish
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify()) # prettify metodi
# 
# # olingan html kod ichidan ma'lum bir klassga ega bo'lganlarini ajratib olish
# news = soup.find_all(class_="news-title")
# print(news[5].text) # ma'lum bir yangilik
# print(len(news)) # uzunligi
# print(news) # barcha yangiliklar
# =============================================================================















