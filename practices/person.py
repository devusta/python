# -*- coding: utf-8 -*-
"""
PRACTICE
MODULE FILE

Created on Mon Feb 26 18:13:37 2024

@author: Asadbek (devusta)
"""

class Person:
    """Person klassi"""
    persons = []
    jobs = {}
    def __init__(self, fname, lname, byear, address, job=''):
        self.fname = fname
        self.lname = lname
        self.byear = byear
        self.address = address
        self.job = job
        Person.persons.append(f"{fname.title()} {lname.title()}")
        Person.jobs[f"{fname.title()} {lname.title()}"] = job
        
    @classmethod 
    def __getitem__(cls, index):
        return cls.persons[index]
    
    def __len__(cls):
        return len(cls.persons)
        
    def __repr__(self):
        return f"{self.fname.title()} {self.lname.title()}"
    
    def get_job(self):
        return self.job.title()

    def get_info(self):
        info = (f"{self.fname.title()} {self.lname.title()}. "
               f"{self.byear}-yilda tug'ilgan. Manzili: {self.address}.")
        info += f" Kasbi {self.job}." if self.job else ""
        return info
    
    
#================================================================================

class Address:
    """Address klassi"""
    def __init__(self, home, street, district, region):
        self.home = home
        self.street = street
        self.district = district
        self.region = region
        
    def __repr__(self):
        return f"{self.region.title()}, {self.district.title()}"
        
    def get_address(self):
        address = (f"{self.region.title()} viloyati, {self.district.title()} tumani, "
                   f"{self.street.title()} ko'cha, {self.home}-uy.")
        return address
        
#=============================================================================    
class Professor(Person):
    """Professor klassi"""
    num_professor = 0
    professors = []
    def __init__(self, fname, lname, byear, address, specialist, experience, job="teacher"):
        super().__init__(fname, lname, byear, address)
        self.specialist = specialist
        self.experience = experience
        self.job = job
        self.students = []
        Professor.num_professor += 1
        Professor.professors.append(f"{fname} {lname}")
        
    def __getitem__(self, index):
        return self.students[index]
        
    def __setitem__(self, index, element):
        self.students[index] = element
    
    def __len__(self):
        return len(self.students)

    def add_student(self, student):
        self.students.append(student)
        

#=============================================================================
class Student(Person):
    """Student klassi"""
    num_students = 0
    def __init__(self, fname, lname, byear, address, id_num, syear, job="talaba"):
        super().__init__(fname, lname, byear, address, job)
        self.id_num = id_num
        self.syear = syear
        self.job = job
        self.subjects = []
        Student.num_students += 1
    
    @classmethod
    def get_num_students(cls):
        return cls.num_students
    
    def __lt__(self, y):
        return self.syear < y.syear
        

    def get_info(self):
        return (f"{self.fname.title()} {self.lname.title()}. {self.byear}-yilda tug'ilgan. "
                f"Manzili: {self.address}. ID raqami: {self.id_num}, {self.syear}-kurs.")
 
class Subject:
    """Subject(fan) klassi"""
    num_subjects = 0
    def __init__(self, name):
        self.name = name
        self.students = []
        Subject.num_subjects += 1
        
    @classmethod
    def get_num_subjects(cls):
        return cls.num_subjects
    
    def __repr__(self):
        return f"{self.name.title()} fani."
        
    def __add__(self, student):
        """Fanga talaba qo'shish"""
        self.add_student(student)
    
    def add_student(self, *students):
        """Fanga talaba qo'shish"""
        for student in students:
            if isinstance(student, Student):
                self.students.append(student)
            else:
                return (f"{student} talaba emas!")
                
    def __sub__(self, student):
        """Fandan talabani o'chirish"""
        if student in self.students:
            self.students.remove(student)
            return f"{self.name} fanidan {student} o'chirildi."
        else:
            return f"{self.name} fanida {student} ismli talaba mavjud emas."
            
    def __len__(self):
        """Fanning talabalar soni"""
        return len(self.students)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
