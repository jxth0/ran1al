from tkinter import *
import customtkinter
from pytube import *

window=customtkinter.CTk()

customtkinter.set_appearance_mode('blue')
customtkinter.set_appearance_mode('system')


window.title(' Donwload Youtube ')
window.geometry('600x250+800+100')
window.resizable(0,0)
window.iconbitmap("C:\\Users\\HUAWEI\\Desktop\\Icon For Program\\You Icon.ico")



def clak1():
    try:
        link=e1.get()
        url=YouTube(link , on_progress_callback=on_progress)
        resandsave=url.streams.get_highest_resolution()
        l1.configure(window , text='Start Download ...')
        l2.configure(window , text= 'Video : '+ resandsave.default_filename)
        resandsave.download("C:\\Users\\HUAWEI\\Desktop")
        l1.configure(window , text='Done Download')

    except:
        l1.configure(window , text='Erorr Download')

# Loding Download 

def on_progress(stream , chunk , bytes_remaining):
    total_size=stream.filesize
    minm_size=total_size - bytes_remaining
    on_my_program= minm_size / total_size * 100 
    done_pro=str(int(on_my_program))
    prog1.configure(text=done_pro+'%')
    prog1.update()
    prog2.set(float(on_my_program) / 100)
e1=customtkinter.CTkEntry(window , width=400)
e1.pack(padx=20,pady=20)

l1=customtkinter.CTkLabel(window , text='')
l1.pack()

l2=customtkinter.CTkLabel(window , text='')
l2.pack()

b1=customtkinter.CTkButton(window , text=' Download ' , command=clak1)
b1.pack()


# Loding Download 

prog1=customtkinter.CTkLabel(window , text='0%')
prog1.pack()

prog2=customtkinter.CTkProgressBar(window , width=300)
prog2.set(0)
prog2.pack(padx=10 , pady=10 )

window.mainloop()