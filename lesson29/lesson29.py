# -*- coding: utf-8 -*-
"""
37-video
29-dars. OOP / OBYEKTLAR BILAN ISHLASH
Created on Sat Feb 24 09:42:36 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # standart arguments
# # get method
# # set method
# =============================================================================


class Student():
    def __init__(self, firstname, lastname, birthyear):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.s_year = 1 # STARDART ARGUMENT 
    
    # SET METHODS / KLASGA MA'LUMOT QO'SHISH METODLARI
    def set_course(self, new_s_year):
        """Talabaning kursini yangilovchi metod"""
        self.s_year = new_s_year
    
    # GET METHODS / KLASDAN MA'LUMOT OLISH METODLARI
    def get_firstname(self):
        """Talabaning ismi"""
        return self.firstname
    
    def get_lastname(self):
        """Talabaning familiyasi"""
        return self.lastname
    
    def get_fullname(self):
        """Talabaning to'liq ismi"""
        return f"{self.firstname.title()} {self.lastname.title()}"
    
    def get_birthyear(self):
        """Talabanning tug'ilan yili"""
        return self.birthyear

    def get_s_year(self):
        """Talabaning kursi"""
        return self.s_year
    
    def get_info(self):
        """Talaba haqida ma'lumot beruvchi metod"""
        return (f"{self.firstname.title()} {self.lastname.title()} "
                f"{self.birthyear}-yilda tug'ilgan. "
                f"{2024-self.birthyear} yoshda va {self.s_year}-kurs.")

student_1 = Student('ahror', 'kamolov', 1997)
student_2 = Student('jamol', 'hoshimov', 1998)
student_3 = Student('jasur', 'akmalov', 2000)

# =============================================================================
# # OBYEKT MA'LUMOTLARINI METODLAR ORQALI EKRANGA CHIQARISH
# print(student_1.get_firstname())
# print(student_1.get_lastname())
# print(student_1.get_fullname())
# print(student_1.get_birthyear())
# print(student_1.get_s_year())
# print(student_1.get_info())
# =============================================================================

# =============================================================================
# # OBYEKT MA'LUMOTINI O'ZGARTIRISH VA YANGI MA'LUMOT QO'SHISH 
# print(student_1.set_s_year(2))
# print(student_1.get_info())
# =============================================================================
    
class Subject():
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.students_quantity = 0
        self.students = []
        
    def add_student(self, student):
        """Fanga talaba qo'shish"""
        self.students.append(student)
        self.students_quantity += 1
        
    def get_name(self):
        """Fanni nomi"""
        return self.subject_name
    
    def get_students_quantity(self):
        """Talabalar soni"""
        return self.students_quantity
    
    def get_students(self):
        """Obyektga tegishli bo'lgan talabalarni ro'yxat shaklida qaytaradi"""
        return [student.get_fullname() for student in self.students]
        
         
subject_1 = Subject('Mathematics')
subject_1.add_student(student_1)
subject_1.add_student(student_2)
subject_1.add_student(student_3)
print(subject_1.subject_name)
print(subject_1.students_quantity)
print(subject_1.get_students()) 

# =============================================================================
# # SEING METHODS OF CLASSES OR OBJECTS
# print(dir(Student))
# 
# def see_methods(klass):
#     """Berilgan klas va obyektning faqat biz yaratgan metod va xususiyatlarini ko'rish"""
#     return [method for method in dir(klass) if method.startswith('__') is False]
# 
# print(see_methods(Student))
# print(see_methods(student_1))
# =============================================================================























