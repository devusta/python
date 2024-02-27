# -*- coding: utf-8 -*-
"""
PRACTICE
MAIN FILE
Created on Mon Feb 26 18:18:25 2024

@author: Asadbek (devusta)
"""
from person import Person, Professor, Address, Student

# Class Address
person1_address = Address(19, 'gulzor', 'paxtabod', 'andijon')
person2_address = Address(21, 'orasta', 'olmaliq', 'toshkent')
pfor1_address = Address(93, 'katta', 'asaka', 'andijon')
prof2_address = Address(101, 'yaxshi', 'jomboy', 'jizzax')
student1_address = Address(39, 'gulshan', 'oltiariq', "farg'ona")
student2_address = Address(31, 'jahon', 'beshariq', "rarg'ona")

# Class Person
person1 = Person('jasur', 'farxodov', 1995, person1_address, 'usta')
person2 = Person('ahror', 'elmurod', 1987, person2_address)
# Class Professor
professor1 = Professor('tohir', 'jalolov', 1977, pfor1_address, 'kimyo', 18)
professor2 = Professor('botir', 'hilolov', 1981, prof2_address, 'matematika', 17)
# Class Student
student1 = Student('hoshim', 'eldorov', 1999, student1_address, 1111111, 3)
student2 = Student('ilhom', 'shomurodov', 1986, student2_address, 1111112, 4)
student3 = Student('javlon', 'kamolov', 1998, student1_address, 1111113, 2)

# =============================================================================
# # Test Person class
# print(person1)             # __repr__ test
# print(person2)         
#  
# print(Person.persons)      # list test
# print(Person.persons[3])
# 
# print(Person.jobs)         # jobs dict test
# 
# print(len(Person.persons)) # __len__ test
# 
# print(student1.get_job())  # get_job() test
# 
# print(person1.get_info())  # get_info() test
# print(person2.get_info())  
# =============================================================================

# =============================================================================
# # Test Address class
# print(person1.address)                  # __repr__ test
# print(student1.address)
# print(person1.address.get_address())    # adress.get_address() test
# print(student1.address.get_address())
# =============================================================================


# print(student1.persons)

# print(Person.jobs)

# professor1.add_student(student1)
# professor1[0] = student2
# print(professor1.students)

# print(student1 < student3)
# print(student1 > student2)
print(person1 != person2)





















































