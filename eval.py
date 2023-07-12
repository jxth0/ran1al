import random
import colorama
from colorama import Back,Fore,Style
def game1 ():
    while True :
        w=input(Fore.BLUE+"ENTER NAME PLAYRER 1 :")
        e=input(Fore.YELLOW+"ENTER NAME PLAYRER 2 :")
        q=int(input(Fore.BLUE+w+" "+"ENTER NUMBER :"))
        z=int(input(Fore.YELLOW+e+" "+"ENTER NUMBER :"))

        print(Fore.BLUE+w+" "+"PLAYER 1 :"+str (q))
        print(Fore.YELLOW+e+" "+"PLAYER 2 :"+str (z))

        if q and z >=6:
            print (Fore.LIGHTBLACK_EX+"ERORR ENTER NUMBER LESS THAN 6 !")
            
            
        elif q >=6:
            print(Fore.LIGHTBLACK_EX+" ENTER NUMBER LESS THAN 6 !")

        elif z >=6:
            print(Fore.LIGHTBLACK_EX+" ENTER NUMBER LESS THAN 6 !")
        
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
            game1()
    
        elif r=="e":
            print("OK SEE YOU LATER ")
            break

        else:
            print("ERORR!")
run=se()