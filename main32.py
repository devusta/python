# -*- coding: utf-8 -*-
"""
40-video
32-dars. DUNDER METODLAR

Created on Sun Feb 25 22:35:01 2024

@author: Asadbek (devusta)
"""

# =============================================================================
# Taqqoslash metodlari:
# x.__lt__(self, y) --->  x < y
# x.__le__(self, y) --->  x <= y 
# x.__gt__(self, y) --->  x > y
# x.__ge__(self, y) --->  x >= y
# x.__eq__(self, y) --->  x == y 
# x.__ne__(self, y) --->  x != y
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


auto1 = Auto('GM', 'Malibu', 'black', 2023, 30000)
auto2 = Auto('Kia', 'K8', 'silver', 2024, 34000)
auto3 = Auto('Hyundai', 'Sonata', 'white', 2024, 29000)

print(auto1 == auto2)
print(auto1 != auto2)
print(auto1 < auto2)
print(auto1 > auto2)
print(auto1 <= auto2)
print(auto1 >= auto2)

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

    
    def add_auto(self, *argument):
        for auto in argument:
            if isinstance(auto, Auto):  # obyektning tegishli yoki yo'qligini aniqlovchi metod
                self.autos.append(auto)
            else:
                print("Avtomobil kiriting!")
                
salon1 = AutoSalon('AutoBox')
salon1.add_auto(auto1, auto2, auto3)
print(len(salon1)) # len list
print(salon1[0])   # get item
print(salon1[:])

# set item
salon1[0] = Auto('Audi', 'A7', 'black', 2024, 37000)
print(salon1[:])








































