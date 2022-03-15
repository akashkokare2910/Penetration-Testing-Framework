from tkinter import *
import os
import tkinter 
# import subprocess 
# subprocess.call('start', shell = True) 


from PIL import ImageTk,Image
from click import style

w=Tk()
w.geometry('1200x700')
w.configure(bg='#262626')
w.resizable(0,0)
w.title('Securezy Pentesting Framework')

def passenc():      
    os.system('python GUI.py')

def pass_manager():
    os.system('python passmanager.py')

def portscan():
    os.system('python portscanner.py')

def portscannerip():
    os.system('start cmd')

def hasher():
    # os.system('start cmd')
    os.system('python hasher.py')
   

# l1=Label(w,text='Hey Securezy\n for you!!',fg='red',bg='#262626', font='times 24 bold italic')
# l1.config(font=('Comic Sans MS',90))
# l1.pack(expand=True)

background_image = tkinter.PhotoImage(file='Text Encryption/Landing_Page1.png')
background_label = tkinter.Label(w, text='Some Plain Text',image=background_image)
background_label.place(relwidth=1, relheight=1)


def toggle_win():
    f1=Frame(w,width=300,height=700,bg='#252d42')
    f1.place(x=0,y=0)




    #buttons
    
    def bttn(x,y,text,bcolor,fcolor,cmd=passenc):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#ede8e8'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#ede8e8'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#ede8e8',
                       border=0,
                       bg=fcolor,
                       activeforeground='#ede8e8',
                       activebackground=bcolor,            
                       command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'TEXT ENCRYPTION/DECRYPTION','#12c48c','#252d42',passenc)
    bttn(0,117,'HASHER','#12c48c','#252d42',hasher)
    bttn(0,154,'PORT SCANNER','#12c48c','#252d42',portscan)
    bttn(0,191,'PASSWORD MANAGER','#12c48c','#252d42',pass_manager)
    bttn(0,228,'IP PORT SCANNING CLI','#12c48c','#252d42',portscannerip)
    # bttn(0,265,'HASHER','#0f9d9a','#12c4c0',None)

    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("Text Encryption/close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#3682f5',
           activebackground='#3682f5').place(x=5,y=10)
    

img1 = ImageTk.PhotoImage(Image.open("Text Encryption/open.png"))

Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)



w.mainloop()