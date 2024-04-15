# -*- coding: utf-8 -*-
"""
OOP bo'limi uchun amaliy topshiriq
Created on Tue Mar 26 12:08:16 2024
                 
@author: Asadbek (devusta)
"""              


class Person:
    def __init__(self, first_name, last_name, age, email, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.__birthday = birthday

    @property
    def birthday(self):
        return list(map(int, self.__birthday.split("-")))

    def get_info(self):
        return (f"{self.first_name.title()} {self.last_name.title()}, "
                f"{self.birthday[0]}-yilda tug'ilgan va {self.age} yoshda. "
                f"Elektron pochta manzili: {self.email}.")

    def get_life_path_number(self):
        num_lst = self.birthday
        sum_num = 0
        while num_lst: sum_num += sum([int(i) for i in str(num_lst.pop(0))])
        return sum([int(i) for i in str(sum([int(i) for i in str(sum_num)]))])
    
    
    def get_info_by_number(self, path_num): 
        with open('life_path.txt', 'r', encoding='utf8') as f:
            num_defs = f.read().split('#')               
        return f"{self.first_name.title()}ning hayot yo'li psixologik jihatdan quyidagicha:\n {num_defs[path_num]}"
           
                

# Obyekt yaratish
person1 = Person("jamshid", "kamolov", 25, "jamshid@email.com", "1999-02-27")
# birthday metodi
print(person1.birthday)
# Obyekt haqida ma'lumot olish
print(person1.get_info())
# Obyektning hayot yo'li raqamini olish
path_num = person1.get_life_path_number()
print(f"Sizning hayot yo'li raqamingiz {path_num}")
# Obyektning hayot yo'li raqamiga mos ma'lumotni chiqarish
print(person1.get_info_by_number(path_num))


    








