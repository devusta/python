# -*- coding: utf-8 -*-
"""
TEST FILE
Created on Mon Mar 18 16:23:25 2024

@author: Asadbek (devusta)
"""
import unittest
from person import *

class PersonTest(unittest.TestCase):
    """Person klassi uchun test"""
    def setUp(self):
        """Test uchun klassga xususiyatlar berish"""
        fname = "jasur"  
        lname = "bahromov"
        fname2 = 'tohir'
        lname2 = 'javlonov'
        byear = 1994
        #Professor class
        specialist = 'chemistry'
        experience = 5
        #Student class
        id_num = 1234567
        syear = 3
        #Address class
        self.address = Address(19, 'gulzor', 'ulugnor', 'andijon')
        self.person1 = Person(fname, lname, byear, self.address)
        self.person2 = Person(fname, lname, byear, self.address, job='usta')
        self.professor1 = Professor(fname, lname, byear, self.address, specialist, experience)   
        self.student1 = Student(fname2, lname2, byear, self.address, id_num, syear)
        
    def test_create(self):
        """Klassning xususiyatlari va berilgan qiymatlarini test qilish"""
        self.assertIsNotNone(self.person1.fname)
        self.assertEqual('jasur', self.person1.fname)
        self.assertIsNotNone(self.person1.lname)
        self.assertEqual('bahromov', self.person1.lname)
        self.assertIsNotNone(self.person1.byear)
        self.assertEqual(1994, self.person1.byear)
        self.assertIsNone(self.person1.job)
        self.assertIsNotNone(self.person2.job)
        self.assertEqual('usta', self.person2.job)
        self.assertEqual(4, len(Person.persons))
        self.assertEqual(2, len(Person.jobs))
        # Professor class
        self.assertIsInstance(self.professor1, Person)
        self.assertEqual(1, Professor.num_professors)
        self.assertEqual(1, len(Professor.professors))
        
        # Student class
        self.assertIsInstance(self.student1, Student)
        self.assertEqual(1, Student.num_students)

    # Metodlarni test qilish
    def test_get_job(self):
        self.assertEqual('Teacher', self.professor1.get_job())
        self.assertEqual('Talaba', self.student1.get_job())
    
    def test_get_info_person(self):
        #1 Kasbi yo'q bo'lsa
        info1 = ("Jasur Bahromov. 1994-yilda tug'ilgan. "
                f"Manzili: {self.address}.")
        self.assertEqual(info1, self.person1.get_info())
        #2 Kasbi bor bo'lsa
        info2 = ("Jasur Bahromov. 1994-yilda tug'ilgan. "
                f"Manzili: {self.professor1.address}."
                " Kasbi teacher.")
        self.assertEqual(info2, self.professor1.get_info())
    
    # Quyida xatolik yuz bermoqda
    # Professor class
    # def test_add_student(self):
    #     self.professor1.add_student(self.student1)
    #     self.assertEqual(self.student1, self.professor1.students[0])
    
    # Student class
    def test_get_info_student(self):
        info3 = ("Tohir Javlonov. 1994-yilda tug'ilgan. "
                 f"Manzili: {self.student1.address}. ID raqami: 1234567,"
                 " 3-kurs.")
        self.assertEqual(info3, self.student1.get_info())
        
    
       

        
unittest.main()

print(Person.persons)
print(Person.jobs)



























