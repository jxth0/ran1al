import pyfiglet
text=pyfiglet.print_figlet(text='@ALI',
                            colors='RED')
while True:
    class IPHONE:
        def __init__(self,name,model,price):
            self.name = name  
            self.model = model
            self.price = price

    mylist = IPHONE('IPHONE 14 PRO','MK699726','$799')

    input1 = input('Enter name or model or price ? , q = Quit :')

    if input1 == 'name' :
        print(mylist.name)

    elif input1 == 'model' :
        print(mylist.model)

    elif input1 == 'price' :
        print(mylist.price)
    
    elif input1 == 'q':
        break

    else :
        print('Erorr')
