# -*- coding: utf-8 -*-
"""
43-video
35-dars. MODUL FILE
Created on Sat Mar 16 16:44:17 2024

@author: Asadbek (devusta)
"""
import json

student2 = {
    'name': "Jasur Hoshimov",
    'birthyear': 1994,
    'is_man': True,
    'syear': 4,
    'family_members': ('father', 'mother', 'sister'),
    'scores': [
        {
            'first_year': {'language': 3, 'math': 3, 'physiology': 5},
            'second_year': {'language': 4, 'math': 3, 'physiology': 4},
            'third_year': {'language': 5, 'math': 4, 'physiology': 5}    
        }
        ],
    'bachelor_warning': 1
    }

student3 = {
    'name': "Mirza Tohirov",
    'birthyear': 1991,
    'is_man': True,
    'syear': 4,
    'family_members': ('father', 'mother', 'sister'),
    'scores': [
        {
            'first_year': {'language': 3, 'math': 3, 'physiology': 5},
            'second_year': {'language': 4, 'math': 3, 'physiology': 4},
            'third_year': {'language': 5, 'math': 4, 'physiology': 5}    
        }
        ],
    'bachelor_warning': 1
    }

with open('student.json') as f:
    student1 = json.load(f)

new_students = [student1, student2, student3]
new_json_files = ['student1.json', 'student2.json', 'student3.json']
n = 0
for file in new_json_files:
    with open(file, 'w') as f:
        json.dump(new_students[n], f)
    n += 1


