from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk

messageinfo=messagebox.showinfo('','1-Ali\n2-Fisal')
print(messageinfo)

class name:
    def __init__(self , name):
        self.name = name

class fisal(name):
    def speak(self):
        return f"{self.name} i like apply"

class ali(name):
    def speak(self):
        return f"{self.name} i like program"

app=ttk.Window('flatly')
app.title('class super')
app.geometry('400x200+800+100')


def job():
    Entry1_get=Entry1.get()
    Entry1_get_lower=Entry1_get.lower()
    
    
    if Entry1_get_lower == 'ali' :
        
        messagebox.showinfo('' , ali.speak())

    elif Entry1_get_lower == 'fisal' :
        
        messagebox.showinfo('' , fisal.speak())

    else:
        
        messagebox.showerror('' , 'Erorr')


Entry1=Entry(width=100)
Entry1.pack(pady=2)


btn=Button(text='Clak Me !' , width=20 , height=1 , command=job)
btn.pack(pady=30)


fisal = fisal("im fisal")
ali = ali("im ali")




app.mainloop()
