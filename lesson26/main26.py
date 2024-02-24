# -*- coding: utf-8 -*-
"""
29-video
26-dars. SO'Z TOPISH O'YINI - AMALIYOT / FIND LETTER GAME
Created on Mon Feb 19 13:23:04 2024

@author: Asadbek (devusta)
"""


import random as r
from uzwords import words


# FUNCTIONS
# FUNCTION 1
def getWord(list):
    """Berilgan har qanday listdan tasodifiy elementni qaytaruvchi funksiya"""
    word = r.choice(list)
    while len(word) > 7:
        word = r.choice(list)
    return word.upper()

# FUNCTION 2
def display(user_letters, word):
    """Kiritilgan harf(lar)ni berilgan so'zda bor yoki yo'qligini aniqlovchi funksiya"""
    display_letter = ''
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter


# FUNCTION 3
def play(list):
    """Berilgan listdagi so'zlardan tasodifiy so'z olib 
    foydalanuvchi bilan so'z topish o'yinini o'ynovchi funksiya"""
    while True:
        word = getWord(list) # FUNCTION 1
        print(word) # SO'ZNI EKRANGA CHIQARISH
        # So'zdagi harflar
        word_letters = set(word)
        # Foydalanuvchi kiritgan harflar
        user_letters = []
        right_letter = []
        wrong_letter = []
        print(f"\nMen {len(word)} xonali so'z o'yladim.\n"
              "U qaysi so'z?")
        i = 0
        while True:
            if i > 0:
                print(f"\n{i}-urinishdagi natija:")
            print(display(user_letters, word))
            if len(user_letters):
                print("\nHozirgacha kiritilgan harflar:")
                for letter in set(user_letters):
                    print(letter, end=', ')
            if not word_letters:
                print(f"\n\nTabriklayman {i} urinishda so'zni topdingiz!")
                break
            elif i == len(word) + 1:
                print(f"\nAfsus, {len(word)} urinishda ham topolmadingiz!"
                      f"\nMen o'ylagan so'z {word} so'zi edi.")
                break
            if i > 0:
                user_letter = input("\n\n1 ta harf kiriting:\n"
                                    ">>>").upper()
                if len(user_letter) > 1:
                    print("\nEndi faqat 1 ta harf kiriting!")
                    continue
            else: 
                user_letter = input(f"\n{len(word)} tagacha harf kiriting!\n"
                                    ">>>").upper()
                if len(user_letter) > len(word):
                    print(f"\nFaqat {len(word)} tagacha harf kiriting!")
                    continue
            if len(user_letter) > 1:
                for letter in user_letter:
                    if letter in word:
                        if letter in word_letters:
                            word_letters.remove(letter)
                            right_letter.append(letter)
                    else:    
                        wrong_letter.append(letter)
                    user_letters.append(letter)
            elif user_letter in user_letters:
                print(f"\n{user_letter} harfi avval kiritilgan!")
                continue
            elif user_letter in word:
                word_letters.remove(user_letter)
                right_letter.append(user_letter)
                user_letters.append(user_letter)
            else: 
                wrong_letter.append(user_letter)
                user_letters.append(user_letter)
            i += 1
            if right_letter:
                for letter in set(right_letter):
                    print(letter, end=' ')
                print("harfi to'g'ri.")
                right_letter.clear()
            if wrong_letter:
                for letter in set(wrong_letter):
                    print(letter, end=' ')
                print("harfi xato.")
                wrong_letter.clear()
    
        answer = input("\nQayta o'ynaysizmi? (yes/no): ")
        if answer == 'no':
            print("TASHAKKUR!")
            break

# PLAY GAME
play(words)
    
    
        






























