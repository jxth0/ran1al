import random
import colorama
from colorama import Back,Fore,Style
from pwinput import pwinput


def game1 ():
    while True :
        w=input(Fore.BLUE+"ENTER NAME PLAYRER 1 :")
        
        q=int(pwinput(Fore.BLUE+w+" "+"ENTER NUMBER :","*"))

        e=input(Fore.YELLOW+"ENTER NAME PLAYRER 2 :")
        
        z=int(pwinput(Fore.YELLOW+e+" "+"ENTER NUMBER :","*"))

        print(Fore.BLUE+w+" "+"PLAYER 1 :"+str (q))
        print(Fore.YELLOW+e+" "+"PLAYER 2 :"+str (z))

        if q and z >=6:
            print (Fore.LIGHTBLACK_EX+"PLEASE ENTER NUMBER LESS THAN 6 !")
            
            
        elif q >=6:
            print(Fore.LIGHTBLACK_EX+" PLEASE ENTER NUMBER LESS THAN 6 !")

        elif z >=6:
            print(Fore.LIGHTBLACK_EX+" PLEASE ENTER NUMBER LESS THAN 6 !")
        
        elif z==q:
            print(Fore.GREEN+"win")
            
            break
        
        else:
            print(Fore.RED+"lose")
            
            break
run=game1()





def se():
    while True:
        r=input(Fore.LIGHTBLACK_EX+"s or e ?:")
        if r=="s":
            run=game1()
    
        elif r=="e":
            print("OK SEE YOU LATER ")
            
            break

        else:
            print("ERORR!")
run=se()
