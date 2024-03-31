# -*- coding: utf-8 -*-
"""
PROPERTY DECORATOR
Created on Sat Mar 30 23:31:38 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # setter
# # setattr()
# # _variable - pastki chiziq boshlangan o'zgaruvchi private o'zgaruvchi
# =============================================================================


# =============================================================================
# # property decorator 1
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#         
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
#     
#     
# human = Celsius()
# human.temperature = 37
# print(human.temperature)
# print(human.to_fahrenheit())
# print(human.__dict__)
# =============================================================================


# =============================================================================
# # protperty decorator 2
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#         
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#     
#     @property 
#     def temperature(self):
#         print("Getting value...")
#         return self._temperature
#     
#     @temperature.setter 
#     def temperature(self, value):
#         print("Setting value...")
#         if value < -273.15:
#             raise ValueError("-273.15 dan kichik harorat mavjud emas.")
#         self._temperature = value
#         
# human = Celsius(37)
# 
# # print(human.get_temperature())
# # print(human.to_fahrenheit())
# 
# print(human.temperature)
# =============================================================================


# =============================================================================
# # propertry decorator 3
# class Member():
#     def __init__(self, height, weight, fat=14.0):
#         self.height = height
#         self.weight = weight
#         self.fat = fat
#         
#     @property 
#     def height(self):
#         return self._height
#     
#     @property 
#     def weight(self):
#         return self._weight
#     
#     @height.setter 
#     def height(self, value):
#         setattr(self, "_height", value)
#         
#     @weight.setter 
#     def weight(self, value):
#         setattr(self, "_weight", value)
#         
#     
# a = Member(170, 75)
# a.height = 190
# print(f"height of a = {a.height}")
# print(f"weight of a = {a.weight}")
# =============================================================================


# =============================================================================
# # Barafsil o'rganish kerak
# # property decorator 4
# class MyProperty:
#     def __init__(self, func):
#         self._func = func
#         
#     def __get__(self, inst, owner=None):
#         return self._func(inst)
# 
# class Location:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         
#     # @property 
#     @MyProperty
#     def loc(self):
#         return [self.x, self.y]
#         
#     def move_left(self):
#         self.x -= 1
# 
#     def move_right(self):
#         self.x += 1
#             
#     def move_up(self):
#         self.y -= 1
#             
#     def move_down(self):
#         self.y += 1
#             
#     def __repr__(self):
#         return f"{type(self).__name__}(x={self.x}, y={self.y})"
#         
#         
# loc = Location()
# loc.move_left()
# loc.move_down()
# print(loc.x)
# print(loc)
# print(loc.loc)
# =============================================================================





























