# -*- coding: utf-8 -*-
"""
FUNCTION DECORATORS
Created on Wed Mar 27 14:53:41 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # Dekoratorlar odatda programmaning bug(xato)sini topishdagi debugging 
# # va funksiyani normal ishlashini tekshirishda hamda funksiyani ishga
# # tushirishdan ma'lumotlarni tekshirishda qo'llaniladi.
# # .format() 
# # help() - dokumentatsiya shaklida yordam olish
# # .join()
# # .split()
# # isinstance() - biror elementni biror obyektga tegishli 
#                # yoki yo'qligi tekshiruvchi funksiya
# # time.sleep() 
# =============================================================================


# =============================================================================
# # function decorator 1
# def my_decorator(func):
#     def wrapper():
#         print("함수 호출 전")
#         func()
#         print("함수 호출 후")
#     return wrapper
# 
# 
# # @my_decorator
# def say_hello():
#     print("안녕하세요!")
#     
# say_hello()
# =============================================================================


# =============================================================================
# # function decorator 2
# def convert_to_int(func):
#     def wrapper(lst):
#         values = func(lst)
#         return int("".join(str(i) for i in values))
#     return wrapper
# 
# 
# @convert_to_int
# def base_func(lst):
#     new_list = []
#     for i in lst:
#         new_list.append(i+1)
#     return new_list
# 
# 
# print(base_func([1, 2, 3]))
# =============================================================================


# =============================================================================
# # function decorator 3
# def upper_result(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper 
# 
# 
# @upper_result 
# def greeting(name: str, surname: str):
#     return f"Hello {name} {surname}"
# 
# 
# @upper_result 
# def greeting2(name: str):
#     return f"Hello {name}"
# 
# 
# # print(greeting("Olim", "Mirzayev"))
# # print(greeting2("Botir"))
# =============================================================================


# =============================================================================
# # function decorator 4
# def join_upper(func):
#     def wrapper(*args, **kwargs):
#         print("upper called:")
#         result = "-".join(func(*args, **kwargs))
#         print("upper returned:")
#         return result.upper()
#     return wrapper
# 
# 
# def get_split(func):
#     def wrapper(*args, **kwargs):
#         print("log called", args)
#         result = func(*args, **kwargs)
#         print("log returned", result)
#         return result.split(" ")
#     return wrapper
# 
# 
# @get_split
# @join_upper 
# def func1(name: str, surname: str):
#     return f"Hello {name} {surname}"
# 
# 
# print(func1("John", "Doe"))
# =============================================================================


import time

# =============================================================================
# # function decorator 5
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         # 함수 실행 전 시간 측정
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         # 함수 실행 후 시간 측정
#         end_time = time.time()
#         # 함수 실행 시간 출력
#         print(f"[알림] 함수명: <{func.__name__}> 실행에"
#               f" {end_time - start_time:.6f} 초 소요되었습니다.")
#         return result
#     return wrapper 
# 
# 
# @timing_decorator 
# def sample_function(n):
#     sum = 0
#     for i in range(n):
#         sum += 1 
#     return sum
# 
# # sample_function 호출
# # print(sample_function(2000000))       
# 
# @timing_decorator
# def another_function():
#     time.sleep(1.5)
#     return 0
# 
# # another_function 호출
# another_function()
# =============================================================================


# =============================================================================
# # function decorator 6
# # 양수인지 확인하는 데코레이터
# def validate_positive_num(func):
#     def wrapper(arg):
#         if arg < 0:
#             raise ValueError("Raqam 0dan katta bo'lishi kerak.")
#         return func(arg)
#     return wrapper 
# 
# 
# # 정수(integer)인지 확인하는 데코레이터
# def validate_integer(func):
#     def wrapper(arg):
#         if not isinstance(arg, int):
#             raise ValueError("Raqam butun bo'lishi kerak.")
#         return func(arg)
#     return wrapper 
# 
# 
# @validate_integer
# @validate_positive_num
# def process_number(num):
#     print(f"숫자 검증: {num}")
#     
#     
# process_number(11)
# =============================================================================


# =============================================================================
# # function decorator 7
# def trace(func):
#     def wrapper():
#         print(func.__name__, "함수 호출 전")
#         func()
#         print(func.__name__, "함수 호출 후")
#     return wrapper 
# 
# 
# @trace
# def hello():
#     print("hello")
#     
# 
# @trace
# def world():
#     print("world")
#     
# 
# hello()
# world()
# =============================================================================


# =============================================================================
# # function decorator 8
# def trace(func):
#     def wrapper(a, b):
#         r = func(a, b)
#         print("{0}(a={1}, b={2}) -> {3}".format(func.__name__, a, b, r))
#         return r
#     return wrapper 
# 
# 
# @trace 
# def add(a, b):
#     return a + b
# 
# 
# print(add(10, 20))
# =============================================================================


# =============================================================================
# # function decorator 9
# def trace(func):
#     def wrapper(*args, **kwargs):
#         r = func(*args, **kwargs)
#         print("{0}(args={1}, kwargs={2}) -> {3}".format(func.__name__, args, kwargs, r))
#         return r
#     return wrapper 
# 
# 
# @trace 
# def get_max(*args):
#     return max(args)
# 
# 
# @trace 
# def get_min(**kwargs):
#     return min(kwargs.values())
# 
# 
# @trace 
# def add(a, b):
#     return a + b
# 
# 
# print(get_max(10, 20))
# print(get_min(x=10, y=20, z=30))
# print(add(12, 23))
# =============================================================================
   

# =============================================================================
# # function decorator 10: 매개변수가 있는 데코레이터
# def is_multiple(x):
#     """매개변수와 반환값을 처리하고 반환값이 매개변수의 
#     배수인지 아닌 지 아렬 주는 펀크션 데코레이터"""
#     def real_decorator(func):
#         def wrapper(a, b):
#             r = func(a, b)
#             if r % x == 0:
#                 print("{0}와 {1}의 합은 {2}의 배수입니다.".format(a, b, x))
#             else:
#                 print("{0}와 {1}의 합은 {2}의 배수가 아닙니다.".format(a, b, x))
#             return f"{a}와 {b}의 합은 {r}입니다."
#         return wrapper 
#     return real_decorator 
# 
# 
# 
# num_a = 5
# num_b = 10
# for i in range(1, 51, 2):
#     @is_multiple(i)
#     def add(a, b):
#         return a + b
#     if (num_a+num_b) % i == 0:
#         print(add(num_a, num_b))
#         
# # print(add(5, 11))
# =============================================================================





















