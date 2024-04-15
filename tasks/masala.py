# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 05:27:24 2024

@author: user
"""


# =============================================================================
# import time
# 
# # function decorator 5
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         # 함수 실행 전 시간 측정
#         start_time = time.time()
#         result = func()
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
# def sample_function():
#     lst_el = get_lst()
#     sum_num = 0
#     while lst_el:
#         sum_num += sum([int(i) for i in str(lst_el.pop(0))])
#     print(sum([int(i) for i in str(sum([int(i) for i in str(sum_num)]))]))
# 
# @timing_decorator
# def sample_function1():
#     lst_el = get_lst()
#     sum_num = 0
#     while lst_el:
#         sum_num += sum([int(i) for i in str(lst_el.pop(0))])
#     print(sum([int(i) for i in str(sum([int(i) for i in str(sum_num)]))]) if sum_num >= 10 else sum_num)
# =============================================================================

# sample_function()
# sample_function1()












