# -*- coding: utf-8 -*-
"""
28-video
25-dars. SON TOP O'YINI / FIND NUMBER GAME
Created on Sun Feb 18 15:38:58 2024

@author: Asadbek (devusta)
"""
import random as r 

# =============================================================================
# FUNCTION 1
def get_answer_user(number):
    """Foydalanuvchiga javob berib, '1', '+', '-' qiymatlarini qaytaruvchi funksiya"""
    for i in range(3):
        answer = input(f"\nSiz {number} sonini o'yladingiz.\n"
              "\nTo'g'ri bo'lsa 1 ni bosing,\n"
              f"O'ylagan soningiz {number} dan kichik bo'lsa '-' kiriting:\n"
              f"{number} dan katta bo'lsa '+' kiriting:>>> ")
        i += 1
        if answer == '1' or answer == '+' or answer == '-':
            break
        else:
            if i <= 3:
                print("\nIltimos, faqat '1', '+' yoki '-' belgilarini kiriting!")
                continue
            break
    return answer

# =============================================================================
# FUNCTION 2
def find_number_user(min, max):
    print(f"\nMen {min} dan {max} gacha son o'ylayman, siz topib ko'ring!")
    number = r.randint(min, max)
    i = 0
    while True:
        if i >= 5:
            print(f"\nAfsuski {i} martada ham topolmadingiz,\n"
                  "Yutqazdingiz!")
            print(f"Men o'ylagan son: {number} edi.")
            break
        if i > 0:
            print("Qayta kiriting!")
        answer = int(input(f"\n{min} va {max} oralig'ida son kiriting: "))
        i += 1
        if answer < min or answer > max:
            print(f"Iltimos, {min} va {max} orasidagi son kiriting!")
        elif number > answer and i < 5:
            print(f"\nXATO. Men o'ylagan son {answer} dan katta.")
        elif number < answer and i < 5:
            print(f"\nXATO. Men o'ylagan son {answer} dan kichik.")
        elif answer == number:
            print(f"\nTabriklayman, {i} urinishda topdingiz!")
            break
    return i

# =============================================================================
# FUNCTION 3     
def find_number_pc(min, max):
    input(f"\nEndi siz {min} dan {max} gacha son o'ylang men topaman!\n"
          "O'ylagan bo'lsangiz boshlash uchun istalgan tugmani bosing.\n")
    min_number = min
    max_number = max
    i = 0
    while True:
        if i >= 5:
            print("\nAfsuski, 5 urinishda ham topolmadim! "
                  "Siz g'olib bo'dingiz!")
            i = 6
            break
        number = r.randint(min_number, max_number)
        answer = get_answer_user(number)
        i += 1
        if answer == '+':
            min_number = number + 1
        elif answer == '-':
            max_number = number - 1
        elif answer == '1':
            print(f"\n{i} urinishda topdim!")
            break
        else:
            print("O'yinni qayta boshlaymiz!")
            break
    return i

# =============================================================================
# FUNCTION 4
def play_again():
    """Foydalanuvchida '1' yoki '0' javobini string shaklda qabul qiluvchi funksiya"""
    for i in range(3):
        answer = input("\nYana o'ynaymizmi?\n"
              "Ha bo'lsa 1, Yo'q bo'lsa 0 ni bosing: ")
        i += 1
        if answer == '1' or answer == '0':
            break
        else:
            if i <= 3:
                print("\nIltimos, 1 yoki 0 ni bosing")
                continue
            print("\nDemak, yana o'ynaymiz!")
            answer = '1'
    return int(answer)

# =============================================================================
# MAIN FUNCTION
def play(min=1, max=10):
    print("\nSiz bilan <SON TOP> o'yini o'ynaymiz!")
    answer = True
    while answer: 
        score_user = find_number_user(min, max) # FUNCTION 2  
        score_pc = find_number_pc(min, max) # FUNCTION 3
        
        if score_user > score_pc:
            print(f"Siz {score_pc}, men {score_user} ta urinish hisobida G'ALABA QILDIM!")
        elif score_user < score_pc:
            print(f"Men {score_pc}, Siz {score_user} ta urinish hisobida G'ALABA QILDINGIZ!")
        else:
            print(f"{score_user}-{score_pc} hisobida durrang qayd etildi!")
        answer = play_again() # FUNCTION 4
        
# =============================================================================

# PLAY GAME
play(10, 20) # MAIN FUNCTION






    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
