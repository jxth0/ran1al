from tkinter import *
from tkinter import messagebox 
import ttkbootstrap as ttk

# class name():
#     def __init__(self,name):
#         self.name=name


# class ali(name):
#     def ali(self):
#         self.name



# class fhad(name):
#     def fhad(self):
#         self.name

# class sami(name):
#     def sami(self):
#         self.name

# aliupdate=ali('ali')
# fhadupdate=fhad('fhad')
# samiupdate=sami('sami')


# print(aliupdate.name)
# print(samiupdate.name)
# print(fhadupdate.name)

class Studint0 ():
    def __init__(self , name , age , Shool_name , cademic_average ):
        self.name = name
        self.age = age
        self.Shool_name = Shool_name
        self.cademic_average = cademic_average



class Fhad(Studint0):
    def Fhad (self , name , age , Shool_name , cademic_average ):
        self.name 
        self.age
        self.Shool_name
        self.cademic_average

# class Sami(Studint0):
#     def Sami (self , name , age , Shool_name , cademic_average ):
#         self.name 
#         self.age
#         self.Shool_name
#         self.cademic_average 

app=ttk.Window(themename='darkly')
app.geometry('450x300+700+200')
app.title('INFO STUDINT')
app.resizable(0,0)

Fhadnami=Fhad('Fhad' , 15  , 'Al-Zinki Secondary School' , '59%')
# Saminame=Sami('Sami' , 19  , 'Al-Zinki Secondary School' , '30%')
studeint1= Studint0('Ali' , 12  , 'Al-Zinki Secondary School' , '98%')

# def zone

def job1 ():
    studint_name=messagebox.showinfo('' , '1-Ali \n1-Fhad')


def job2 ():
    en1=entry.get()
                
    if en1 == '1' :
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , studeint1.name)
    
    elif  en1 == '2' :
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , studeint1.age)

    elif en1=='3':
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , studeint1.Shool_name)

    elif en1 == '4':
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , studeint1.cademic_average)
    
    if en1 == '5' :
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , Fhadnami.name)
    
    elif  en1 == '6' :
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , Fhadnami.age)

    elif en1=='7':
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , Fhadnami.Shool_name)

    elif en1 == '8':
        Text1.delete(1.0 , END)
        Text1.insert(1.0 , Fhadnami.cademic_average)
    else:
        messagebox.showerror('' , 'Erorr')
        

def job3():
   messagebox.showinfo('' ,'1-name (for ali)\n2-Age (for ali)\n3-Shool name (for ali)\n4-cademic average (for ali)\n5-name (for fhad)\n6-Age (for fhad)\n7-Shool name (for fhad)\n8-cademic average (for fhad)')


entry=Entry(width=80)
entry.pack()

Text1=Text(width=40, height=3)
Text1.pack(pady=5)


label21= Label(text='ادخل بالرقم ولاتكتب (مثال 1=الاسم) وهكذا \nاضغط على what i can serch  لتعرف ترتيب الارقام وماذا يفعل كل رقم')
label21.pack()


Button2=Button(text='Serch' , command=job2 , width=20 )
Button2.pack(pady=4)


Button1=Button(text='Name Studint' , command=job1 , width=20)
Button1.pack(pady= 10)


Button3=Checkbutton(text='What i Can Serch ?' , command=job3)
Button3.pack(pady=9)

app.mainloop()
