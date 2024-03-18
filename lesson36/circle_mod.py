# -*- coding: utf-8 -*-
"""
44-video
36-dars. MODUL FILE
Created on Sun Mar 17 12:29:09 2024

@author: Asadbek (devusta)
"""
def get_area(r, pi=3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def get_perimeter(r, pi=3.14159):
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2*pi*r

def tub_sonmi(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
        
# AMALIYOT
# eng katta son
def get_largest_number(num1, num2, num3):
    """Berilgan sonlarning eng kattasini qytaruvchi funksiya"""
    larger = num2 if num1 < num2 else num1
    largest = num3 if larger < num3 else larger 
    return largest

# katta harfga almashtirish
def change_letter(list_name):
    """Berilgan listdagi har bir matnni bosh harfda qaytaruvchi funksiya"""    
    return [item.title() for item in list_name]
    
fruits = ['anjir', 'olcha', 'bodom']
new_fruits = ['Anjir', 'Olcha', 'Bodom']

# juft son
def get_even_num(num_list):
    """berilgan listdagi sonlar ichidan faqat juftlarini qaytaruvchi funksiya"""
    return [item for item in num_list if item % 2 == 0]

numbers = [23, 42, 77, 62, 98, 99]
even_numbers = [42, 62, 98]

# fibonacci sonlar
def is_fibonacci(num):
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return num in fib

    
    
    
    
    
    
    
    
    
    
    
    
