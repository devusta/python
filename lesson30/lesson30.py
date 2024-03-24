# -*- coding: utf-8 -*-
"""
38-video
30-dars. VORISLIK VA POLIMORFIZM
Created on Sat Feb 24 23:27:14 2024

@author: Asadbek (devusta)
"""
# =============================================================================
# # ✅NEW UNDERSTANDINGS
# # inheritance - bir(super) klasdan boshqa bir voris klas yaratish
# # polimorfizm - super klas metodlarini voris klas uchun qayta yozish
# =============================================================================

# SUPER CLASS
class Person:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, firstname, lastname, passport, birthyear):
        """Shaxsning xususiyatlari"""
        self.firstname = firstname
        self.lastname = lastname
        self.__passport = passport
        self.__birthyear = birthyear
        
    def get_fullname(self):
        return f"{self.firstname.title()} {self.lastname.title()}"
        
    def get_info(self):
        info = (f"{self.firstname.title()} {self.lastname.title()}. "
                f"Passport raqami: {self.passport}, {self.birthyear}-yilda tug'ilgan.")
        return info
    
    def get_age(self, current_year):
        """Shaxsning yoshi"""
        return current_year - self.birthyear

person_1 = Person('shavkat', 'kamolov', 'AB1234567', 1987)
person_2 = Person('jamol', 'kozimov', 'AB1234567', 1990) 
# print(person_1.get_info())
# print(person_1.get_age(2024))

# =======================================================================
# INHERITOR CLASS
class Student(Person):
    """Talaba klassi"""
    __num_students = 0
    def __init__(self, firsname, lastname, passport, birthyear, id_number, address):
        super().__init__(firsname, lastname, passport, birthyear) #IHERITANCE
        self.__id_number = id_number
        self.s_year = 1 
        self.address = address
        self.subjects = []
        Student.__num_students += 1
    
    @classmethod
    def get_num_students(cls):
        return cls.__num_students
       
    def get_id_number(self):
        """Talaba ID raqami"""
        return self.__id_number
    
    def get_s_year(self):
        """Talaba o'qish bosqichi"""
        return self.s_year
    # POLIMORFIZM
    def get_info(self):
        info = (f"{self.firstname.title()} {self.lastname.title()}. "
                f"Passport raqami: {self.passport}, {self.birthyear}-yilda tug'ilgan. "
                f"ID raqam: {self.id_number}, {self.s_year}-kurs.")
        return info

    def apply_subject(self, sub_name):
        """Talabani fanga yozish"""
        self.subjects.append(sub_name)
        return f"Siz {Subjects.get_sub_name(sub_name).title()} faniga a'zo bo'ldingiz."
        
    def get_subjects(self):
        """Talaba yozilgan fanlarni ko'rish"""
        return [Subjects.get_sub_name(subject) for subject in self.subjects]
         
    
    def remove_subject(self, sub_name):
        """Talaba yozilgan fanni o'chirish"""
        if sub_name in self.subjects:
            self.subjects.remove(sub_name)
            return f"{Subjects.get_sub_name(sub_name).title()} fani ro'yxatdan o'chirildi."
        else:
            return f"Siz {Subjects.get_sub_name(sub_name).title()} faniga yozilmagansiz."
            
        

# KLASS ICHIDAGI XUSUSIYATLARNI ALOHIDA KLASS SHAKLIDA YARATISH
class Address:
    """Manzil yaratuvchi klass"""
    def __init__(self, home, street, district, region):
        self.home = home
        self.street = street
        self.district = district
        self.region = region
    
    def get_address(self):
        """Manzilni ko'rish"""
        address = (f"{self.region.title()} viloyati, {self.district.title()} tumani, "
                   f"{self.street.title()} ko'chasi, {self.home}-uy.")
        return address
    
student_1_address = Address(17, 'orasta', 'ulugnor', 'andijon')
student_2_address = Address(21, 'olmazor', 'baliqchi', 'andijon')
student_1 = Student('kamol', 'jamolov', 'AB1234567', 1998, 1234567, student_1_address)
student_2 = Student('tohir', 'komilov', 'AB1234567', 1996, 1234567, student_2_address)

# print(Student.get_num_students())
# print(student_1.get_info(), student_1.address.get_address())

class Subjects:
    """Fanlar klassi"""
    def __init__(self, sub_name):
        self.sub_name = sub_name
        
    def get_sub_name(self):
        return self.sub_name
        
# Create the new object
math = Subjects('mathematics')
lang = Subjects('language')
liter = Subjects('literature')
culture = Subjects('culture')

student_1.apply_subject(math) # Talabaning fanlariga yangi fan qo'shish
student_1.apply_subject(lang)
# print(student_1.apply_subject(liter)) 
# print(student_1.remove_subject(culture)) # Talabaning fanlaridan biror fanni o'chirish
# print(student_1.remove_subject(math))
# print(student_1.get_subjects()) # Talabaning fanlarini ko'rish

# =============================================================================
# Inheritor class
class Professor(Person):
    """Professor klassi"""
    def __init__(self, firstname, lastname, passport, birthyear, experience, specialist):
        super().__init__(firstname, lastname, passport, birthyear)
        self.experience = experience
        self.specialist = specialist
        self.students = []
    
    def get_experience(self):
        return self.experience
    
    def get_specialist(self):
        return self.specialist.title()
    
    def add_student(self, new_student):
        self.students.append(new_student)
        return f"{new_student.get_fullname()} guruhingizga qo'shildi."
        
    def get_info(self):
        return (f"{self.firstname.title()} {self.lastname.title()}. "
                f"Passport number: {self.passport}, {self.birthyear}-yilda tug'ilgan. "
                f"Mutaxassisligi {self.specialist}, tajribasi {self.experience} yil.")

    def get_students(self):
        return [student.get_fullname() for student in self.students]
        

professor1 = Professor('hoshim', 'ilhomov', 'AB1234567', 1987, 5, 'kimyo')
professor2 = Professor('jamol', 'kamolov', 'AB1234567', 1977, 18, 'matematika')

# print(professor1.get_info())
# print(professor1.get_experience())
# print(professor1.get_specialist())
# print(professor1.add_student(student_1))
# print(professor1.add_student(student_2))
# print(professor1.get_students())

# =============================================================================
# Inheritor class
class Rector(Professor):
    """Rector klassi"""
    def __init__(self, firstname, lastname, passport, birthyear, experience, specialist, rank):
        super().__init__(firstname, lastname, passport, birthyear, experience, specialist)
        self.rank = rank    
        self.professors = []
    
    def get_rank(self):
        return self.rank
    
    def add_student(self, professor, new_student):
        professor.add_student(new_student)
        return (f"{professor.get_fullname()} guruhiga "
                f"{new_student.get_fullname()} qo'shildi.")
    
    def remove_student(self, professor, student):
        professor.students.remove(student)
        return (f"{professor.get_fullname()} guruhidagi "
                f"{student.get_fullname()} o'qishdan chetlashtirildi.")
    
    def get_students(self, professor):
        return [student.get_fullname() for student in professor.students]
    
    def add_professor(self, professor):
        self.professors.append(professor)
        return f"{professor.get_fullname()} ismli professor ishga olindi."
        
    def fire_professor(self, professor):
        self.professors.remove(professor)
        return f"{professor.get_fullname()} ishdan chetlatildi."
        
    def get_professors(self):
        return [professor.get_fullname() for professor in self.professors]
    
    def get_info(self):
        return (f"{self.firstname.title()} {self.lastname.title()}. "
                f"Passport number: {self.passport}, {self.birthyear}-yilda tug'ilgan. "
                f"Mutaxassisligi {self.specialist}, tajribasi {self.experience} yil. "
                f"{self.rank} unvoniga ega.")
    
rektor = Rector('eldor', 'jasurov', 'AB1234567', '1978', 28, 'kimyo', 'Akademik')        

# =============================================================================
# # About rector
# print(rektor.get_fullname())
# print(rektor.get_rank())
# print(rektor.get_specialist())
# print(rektor.get_experience())
# print(rektor.get_info())
# 
# # Add student
# print(rektor.add_student(professor1, student_1))
# print(rektor.add_student(professor1, student_2))
# print(rektor.add_student(professor2, student_1))
# print(rektor.add_student(professor2, student_2))
# # To see Students
# print(rektor.get_students(professor1))
# print(rektor.get_students(professor2))
# 
# # Remove students
# print(rektor.remove_student(professor1, student_1))
# print(rektor.remove_student(professor2, student_2))
# # To see Students
# print(rektor.get_students(professor1))
# print(rektor.get_students(professor2))
# 
# # Add rofessor
# print(rektor.add_professor(professor1))
# print(rektor.add_professor(professor2))
# # To see Professors
# print(rektor.get_professors())
# 
# # Fire professor
# print(rektor.fire_professor(professor1))
# # To see Professors
# print(rektor.get_professors())
# =============================================================================












