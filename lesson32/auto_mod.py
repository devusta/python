# -*- coding: utf-8 -*-
"""
Auto MODUL
Created on Wed Feb 28 01:38:28 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # dir() - obyektning maxsus xususiyatlarini ko'rish uchun funksiya
# # __str__() - obyekt haqida ma'lumot olish. Faqat str va print bilan ishlaydi
# # __repr__() - obyekt haqida ma'lumot olish metodi. Barcha ma'lumot turlari bilan ishlaydi
# # __len__() - obyektning uzuligi
# # __getitem__() - 
# # __setitem__() - 
# # __call__() - obyekt haqida ma'lumot olish metodi
# # __lt__(self, y) - x < y
# # __le__(self, y) - x <= y 
# # __gt__(self, y) - x > y
# # __ge__(self, y) - x >= y
# # __eq__(self, y) - x == y
# # __ne__(self, y) - x != y
# # isinstance() - obyektni qandaydir klassga tegishli yoki yo'qligini tekshirish
# # __getitem__() - ro'yxatdagi ma'lum elementni ko'rish
# # __setitem__() - ro'yxatga ma'lum element qo'shish 
# # __call__() 
# # __add__()
# # __sub__()
# =============================================================================


class Auto:
    __num_auto = 0
    def __init__(self, maker, model, color, year, price):
        self.maker = maker
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        Auto.__num_auto += 1
        
    # Dunder method
    def __repr__(self):   # =__str__
        return f"Avto: {self.maker} {self.model}"

    def __eq__(self, y):
        return self.price == y.price
    
    def __lt__(self, y):
        return self.price < y.price
    
    def __le__(self, y):
        return self.price <= y.price
    
    

class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.autos = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        """Obyektga tegishli ma'lum ro'yxatning uzunligi"""
        return len(self.autos)
    
    def __getitem__(self, index):
        """Obyektga tegishli ma'lum ro'yxatdagi elementlarni ko'rish"""
        return self.autos[index]
    
    def __setitem__(self, index, element):  
        self.autos[index] = element
        
    def __call__(self, *args):     
        """Bu metodga har qanday amal uchun kod yozish mumkin"""
        if args:
            for auto in args:
                self.add_auto(auto)
        return [auto for auto in self.autos]

    def __add__(self, y):
        if isinstance(y, AutoSalon):
            new = AutoSalon(f"{self.name} {y.name}")
            new.autos = self.autos + y.autos
            return new
        elif isinstance(y, Auto):
            self.add_auto(y)        
    
    def add_auto(self, *args):
        for auto in args:
            if isinstance(auto, Auto):  # obyektning tegishli yoki yo'qligini aniqlovchi metod
                self.autos.append(auto)
            else:
                print("Avtomobil kiriting!")
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

