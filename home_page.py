from tkinter import *
import os
import tkinter 


from PIL import ImageTk,Image
from click import style

w=Tk()
w.geometry('1100x700')
w.configure(bg='#262626')
w.resizable(0,0)
w.title('Securezy Pentesting Framework')

def passenc():
    os.system('python GUI.py')

def passmanager():
    os.system('python passmanager.py')

def portscan():
    os.system('python portscanner.py')
   

l1=Label(w,text='Hey Securezy\n for you!!',fg='red',bg='#262626', font='times 24 bold italic')
l1.config(font=('Comic Sans MS',90))
l1.pack(expand=True)

background_image = tkinter.PhotoImage(file='Text Encryption/hacking.png')
background_label = tkinter.Label(w, text='Some Plain Text',image=background_image)
background_label.place(relwidth=1, relheight=1)


def toggle_win():
    f1=Frame(w,width=300,height=700,bg='#12c4c0')
    f1.place(x=0,y=0)




    #buttons
    
    def bttn(x,y,text,bcolor,fcolor,cmd=passenc):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                       command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'TEXT ENCRYPTION/DECRYPTION','#0f9d9a','#12c4c0',passenc)
    bttn(0,117,'PASSWORD CRACKING','#0f9d9a','#12c4c0',None)
    bttn(0,154,'PORT SCANNING','#0f9d9a','#12c4c0',portscan)
    bttn(0,191,'PASSWORD MANAGER','#0f9d9a','#12c4c0',passmanager)
    # bttn(0,228,'XXXXX','#0f9d9a','#12c4c0',None)
    # bttn(0,265,'XXXX','#0f9d9a','#12c4c0',None)

    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("Text Encryption/close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

img1 = ImageTk.PhotoImage(Image.open("Text Encryption/open.png"))

Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)



w.mainloop()