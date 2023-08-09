from tkinter import*
from tkinter import messagebox

GUI=Tk()

GUI.title('TEST 7')

GUI.geometry('250x350')
GUI.resizable(False,False)

e1=Entry(GUI,width=25)
e1.pack()

def click():
    messagebox.showinfo('INFO',e1.get())

b1=Button(GUI,text="ENTER ",command=click)
b1.pack()



GUI.mainloop()