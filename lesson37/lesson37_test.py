# -*- coding: utf-8 -*-
"""
45-video
37-dars. KLASSLARNI TEKSHIRISH / MODUL FILE
Created on Sun Mar 17 22:18:09 2024

@author: Asadbek (devusta)
"""
import unittest
from lesson37 import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        """Test uchun xususiyatlar berish"""
        maker = "GM"
        model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.auto1 = Car(maker, model, year)
        self.auto2 = Car(maker, model, year, price=self.price)

    def test_create(self):
        """Klassning xususiyatlari va berilgan qiymatlarini test qilish"""
        # Qiymat mavjudligini assertIsNotNone metodi bilan test qilamiz
        self.assertIsNotNone(self.auto1.maker)
        self.assertIsNotNone(self.auto1.model)
        self.assertIsNotNone(self.auto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan test qilamiz
        self.assertIsNone(self.auto1.price)
        # Qiymat tengligini assertEqual metodi bilan test qilamiz
        self.assertEqual(0, self.auto1.get_km())
        # auto2 narxini test qilamiz
        self.assertEqual(self.price, self.auto2.price)
        
    # Klassning metodlarini test qilish
    def test_set_price(self):
        new_price = 45000
        self.auto2.set_price(new_price)
        self.assertEqual(new_price, self.auto2.price)
        
    def test_add_km(self):
        #1 Musbat qiymat berib test qilish
        self.auto1.add_km(self.km)
        self.assertEqual(self.km, self.auto1.get_km())
        self.auto1.add_km(5000)
        self.assertEqual(15000, self.auto1.get_km())
        #2 Manfiy qiymat berib test qilish
        new_km = -5000
        try:
            self.auto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
unittest.main()



























