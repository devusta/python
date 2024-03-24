# -*- coding: utf-8 -*-
"""
36-video
28-dars. KLASSLAR / OOP

Created on Sat Feb 24 07:59:37 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # OOP - Object Oriented Programming
# # class
# # self 
# =============================================================================

# =============================================================================
# # CREATE A NEW CLASS
class Student: 
     def __init__(self, name, lastname, birthday):
         self.name = name
         self.lastname = lastname
         self.birthday = birthday
    
     def get_name(self):
         return self.name
     
     def get_lastname(self):
         return self.lastname
     
     def get_age(self, year):
         return year - self.birthday
     
     def about_student(self):
         return (f"Ismim {self.name.title()}, familiyam {self.surname.title()} "
                 f"va {2024 - self.birthday} yoshdaman.")      
# =============================================================================

# =============================================================================         
# # CREATE NEW OBJECTS USING CLASS
student_1 = Student("olim", "qosimov", 2001)
student_2 = Student("kozim", "jalolov", 1998)
student_3 = Student("javohir", "kamolov", 1994)
 
 # USING CLASS AND OBJECT
print(student_1.name)
 
print(student_2.get_age(2024))

print(student_1.about_student())
# =============================================================================



























































