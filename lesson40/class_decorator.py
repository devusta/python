# -*- coding: utf-8 -*-
"""
CLASS DECORATORS
Created on Wed Mar 27 23:06:44 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # @property decorator qabul qilgan metod argument qabul qilmaydi
# =============================================================================


# =============================================================================
# # class decorator 1
# class Trace:
#     """함수를 매개변수로 받는 클래스"""
#     def __init__(self, func):
#         self.func = func
#         
#         
#     def __call__(self):
#         print(self.func.__name__, "함수 시작")
#         self.func()
#         print(self.func.__name__, "함수 끝")
# 
# 
# @Trace
# def greet():
#     print("Hello")
#     
#     
# greet()
# =============================================================================


# =============================================================================
# # class decorator 2
# class Trace:
#     def __init__(self, func):
#         self.func = func
#         
#     
#     def __call__(self, *args, **kwargs):
#         r = self.func(*args, **kwargs) # 가변 인수
#         print("{0}(args={1}, kwargs{2}) -> {3}"
#               .format(self.func.__name__, args, kwargs, r))
#         return r
#     
#     
# @Trace 
# def add(a, b):
#     return a + b
# 
# 
# print(add(12, 13))
# print(add(a=15, b=27)) # 가변 이수
# =============================================================================


# =============================================================================
# # class decorator 3
# class IsMultiple:
#     """매개변수와 반환값을 처리하고 반환값이 매개변수의
#     배수인지 아닌 지 알려주는 클래스 데코레이터"""
#     def __init__(self, x):
#         self.x = x
#         
#     
#     def __call__(self, func):
#         def wrapper(a, b):
#             r = func(a, b)
#             if r % self.x == 0:
#                 print(f"{a}하고 {b}의 합은 {self.x}의 배수입니다.")
#             else:
#                 print(f"{a}하고 {b}의 합은 {self.x}의 배수가 아닙니다.")
#             return f"{a}하고 {b}의 합은 {r}입니다."
#         return wrapper
# 
# 
# @IsMultiple(3)
# def add(a, b):
#     return a + b
# 
# 
# print(add(14, 19))
# print(add(55, 99))
# =============================================================================

















