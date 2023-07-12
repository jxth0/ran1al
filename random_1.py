import random
def game1 ():
    while True :
        a="12345"
        q=int(input("ENTER NUMBER :"))
        z=int(random.choice(a))

        print("YOU :"+str (q))
        print("PC :"+str (z))

        if q ==z:
            print ("WIN")
            break
            
        elif q >=6:
            print("ERORR ENTER NUMBER LESS THAN 6 !")

        else:
            print("lose")
        
run=game1()

def se():
    while True:
        r=input("s or e ?:")
        if r=="s":
            game1()
    
        elif r=="e":
            print("OK SEE YOU LATER ")
            break

        else:
            print("ERORR!")
run=se()