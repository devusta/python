# -*- coding: utf-8 -*-
"""
44-video
36-dars. FUNKSIYALARNI TEKSHIRISH. TEST FILE
Created on Sun Mar 17 10:39:34 2024

@author: Asadbek (devusta)
"""
# ✅NEW UNDERSTANDINGS:
# unittest - kodlarni tekshirish uchun modul
# TestCase - unittestdagi test classi. Biz yozgan test classlar
#            shu klassdan meros oladi
# assertEqual - unittestdagi tenglikni taqqoslovchi metod
# assertAlmostEqual - unittestdagi tenglikning ma'lum 
#                     darajasigacha tekshiruvchi metod
#                     Matematik amallar bilan ishlatiladi
# assertNotEqual(a, b) - a != b
# assertTrue(x) - x ning qiymati True
# assertFalse(x) - x ning qiymati False
# assertIs(a, b) - a bu b
# assertIsNot(a, b) - a bu b emas
# assertIsNone(x) - x ning qiymati None
# assertIsNotNone(x) - x ning qiymati None emas
# assertIn(a, b) - a b ning ichida
# assertNotIn(a, b) - a b ning ichida emas
# assertIsInstance(a, b) - a b ning vorisi
# assertNotIsInstance(a, b) - a b ning vorisi emas

import unittest
from name_mod import get_full_name

class NameTest(unittest.TestCase): # unittestning TestCase klassidan meros olib yangi klass yaratish
    def test_full_name(self):
        name = get_full_name('alijon', 'valiyev')
        self.assertEqual(name, 'Alijon Valiyev')
        
    def test_given_name(self):
        name = get_full_name('alijon', 'valiyev', 'tohirovich')
        self.assertEqual(name, 'Alijon Tohirovich Valiyev')
unittest.main()








































