# -*- coding: utf-8 -*-
"""
42-video
34-dars. JSON(JavaScript Object Notation)
Created on Sat Mar  2 21:36:01 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS:
# # dumps() - obyektni json formatga o'tkazish
# # dump()  - obyekt(ma'lumot)ni json faylga saqlash(qo'shish)
# # loads() - json formatdagi obyektni pythonga o'tkazish
# # indent - xatboshi tashlash
# =============================================================================

# Modul JSON
import json

# =============================================================================
# # Butun sonni jsonga saqlash
# x = 10
# x_json = json.dumps(x)
# print(x)
# print(type(x))
# print(x_json)
# print(type(x_json))
# =============================================================================

# =============================================================================
# # O'nlik sonni jsonga o'tkazish
# y = 5.5
# y_json = json.dumps(y)
# print(y)
# print(type(y))
# print(y_json)
# print(type(y_json))
# =============================================================================

# =============================================================================
# # Booleanni jsonga o'tkazish
# m = True
# m_json = json.dumps(m)
# print(m)
# print(type(m))
# print(m_json)
# print(type(m_json))
# =============================================================================

# =============================================================================
# # tuple() ni jsonga o'tkazish
# numbers = (12, 45, 23, 76)
# numbers_json = json.dumps(numbers)
# print(numbers)
# print(type(numbers))
# print(numbers[0])
# 
# print(numbers_json)
# print(type(numbers_json))
# print(numbers_json[0])
# 
# # json'ga o'tkazilgan tuple'ni qaytarib pythonga o'tkazganimizda
# # list bo'lib o'tadi
# numbers2 = json.loads(numbers_json)
# print(numbers2)
# print(type(numbers2))
# =============================================================================

# =============================================================================
# # lug'atni jsonga o'tkazish
# patient = {
#     "name": "Tohir Eldorov", 
#     "age": 30,
#     "is_married": True,
#     "children": ("Ahmad", "Bonu"),
#     "allergy": None, 
#     "drugs": [
#         {"name": "Analgin", "quantity": 5.0},
#         {"name": "Panadol", "quantity": 1.2},
#         ]
#     }
# 
# patient_json = json.dumps(patient, indent=4)
# print(patient_json)
# 
# # jsonga o'tkazilgan lug'atni pythonga qaytarib o'tkazish
# patient1 = json.loads(patient_json)
# print(patient1)
# print(type(patient1))
# print(patient.keys())
# print(patient1['drugs'])                
# print(patient1['drugs'][0])            
# print(patient1['drugs'][0]['name'])     
# print(patient1['drugs'][0]['name'][0])
# =============================================================================

# =============================================================================
# # obyektni json faylga saqlash(yozish)
# student = {
#     'name': 'Olim Mirzayev',
#     'birthyear': 1993,
#     'is_man': True,
#     'syear': 3,
#     'family_members': ('father', 'mother', 'brother', 'sister'),
#     'scores': [
#         {
#             'first_year': {'language': 4, 'math': 5, 'physiology': 4},
#             'second_year': {'language': 5, 'math': 4, 'physiology': 4},
#             'third_year': {'language': 5, 'math': 3, 'physiology': 5}
#          }
#         ],
#     'bachelor_warning': None
#     }
# 
# with open('student.json', 'w') as f:
#     json.dump(student, f)
# =============================================================================
    
# =============================================================================
# # json faylni pythonda ochish va o'zgaruvchiga yuklash
# with open('student.json') as f:
#     student_info = json.load(f)
#     print(type(f))
# 
# print(student_info)
# print(type(student_info))
# =============================================================================

# =============================================================================
# # obyektni json formatda python o'zgaruvchiga saqlash
# student = {
#     'name': 'Olim Mirzayev',
#     'birthyear': 1993,
#     'is_man': True,
#     'syear': 3,
#     'family_members': ('father', 'mother', 'brother', 'sister'),
#     'scores': [
#         {
#             'firts_year': {'language': 4, 'math': 5, 'pysiology': 4},
#             'second_year': {'language': 5, 'math': 4, 'pysiology': 4},
#             'third_year': {'language': 5, 'math': 3, 'pysiology': 5}
#           }
#         ],
#     'bachelor_warning': None
#     }
# 
# student_json = json.dumps(student)
# print(student_json)
# print(type(student_json))
#     
# # json formatdagi o'zgaruvchini oddiy o'zgaruvchiga o'tkazish
# student2 = json.loads(student_json)
# print(student2)
# print(type(student2))
# =============================================================================

# =============================================================================
# # AMALIYOT
# with open('api-result.json', 'r') as f:
#     file_info = json.load(f)
#     
# # print(file_info)
# keys = [key for key in file_info.keys()]
# print(len(keys))
# print(keys[0])
# print(keys[1])
# print(file_info['query']['pages']['13801']['title'])
# print(file_info['query']['pages']['13801']['extract'])
# 
# # print(file_info.values())
# =============================================================================

  































































