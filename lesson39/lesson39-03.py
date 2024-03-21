# -*- coding: utf-8 -*-
"""
47-video
39-03-dars. PYTHON TASHQI KUTUBXONASI
            WordCluod MODULI
            OpenCV MODULI
Created on Thu Mar 21 13:23:50 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # WordCloud - matn ichida eng ko'p uchragan matnlarni bulu 
#             # ko'rinishida qaytaruvchi modul
# # matplotlib.pyplot
# # openCV - turlli xil tasvirlar bilan ishlash uchun modul
# # cv2
# =============================================================================


import requests
from pprint import pprint
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# =============================================================================
# # WordCloud yordamida kun.uz sahifasidagi eng ko'p foydalanilgan so'zlar
# # bulut ko'rinishida chiqarish
# webpage = "https://kun.uz/news/main"
# r = requests.get(webpage)
# # pprint(r.text)
# 
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())
# 
# news = soup.find_all(class_='news-title')
# matn = ""
# for n in news:
#     matn += n.text
#     
# stopwords = ["uchun", "bo'yicha", "lekin", "bilan", "va", "bor", "ham", "xil", "yil"]
# wordcloud = WordCloud(width = 1000, height = 1000, background_color = 'white',
#                       stopwords = stopwords, min_font_size = 20).generate(matn)
# 
# # plot the WordCloud image
# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad = 0)
# plt.show()
# =============================================================================

# OpenCV moduli
import cv2 

# =============================================================================
# # copyright Tim Ruscia aka techwithtim
# # code from https://github.com/techwithtim/OpenCV-Tutorials
# 
# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# 
# while True:
#     ret, frame = cap.read()
# 
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y:y+w, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
# 
#     cv2.imshow('frame', frame)
# 
#     if cv2.waitKey(1) == ord('q'):
#         break
# 
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================












