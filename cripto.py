from tkinter import *
from tkinter import Text
from criptofunction import cipher
from PIL import ImageTk,Image
import string

#main window
root = Tk()
root.title("Cripto")
root.iconbitmap('photos/criptologo.ico')
root.geometry("750x450")
root.minsize(300, 200)
root.configure(background='#215153')

#functions for code and decode
def startcode():
    decode.delete('1.0','end')
    decode.insert('1.0', cipher(code.get('1.0',END),key.get(),'c'))
    return

def startdecode():
    code.delete('1.0','end')
    code.insert('1.0', cipher(decode.get('1.0',END),key.get(),'d'))
    return


#title
p_title=Label(root,text="\nWelcome to Cripto 1.0\n\nWith this program you can code your messages and decode it! Try it with your friends!\n")
p_title.configure(background='#4d5753',foreground='#96cdc9')


p_title.place(relx=0.5,rely=0,anchor='n',relheight=0.15,relwidth=1.0)

#text labels
p_t1=Label(root,text='DECODED')
p_t2=Label(root,text='CODED')
p_t1.configure(background='#215153',foreground='#96cdc9')
p_t2.configure(background='#215153',foreground='#96cdc9')

p_t1.place(relx=0.25,rely=0.175,anchor='n')
p_t2.place(relx=0.75,rely=0.175,anchor='n')

#text boxes
code=Text(root,width=50,background='#4d5753',foreground='#96cdc9')
decode=Text(root,width=50,background='#4d5753',foreground='#96cdc9')

code.place(relx=0.25,rely=0.25,anchor='n',relwidth=0.4,relheight=0.4)
decode.place(relx=0.75,rely=0.25,anchor='n',relwidth=0.4,relheight=0.4)
            
#code & decode button
start1=Button(root,text='CODE',padx=10,pady=10,command=startcode)
start2=Button(root,text='DECODE',padx=10,pady=10,command=startdecode)
start1.configure(background='#588e84',activebackground='#54958a',borderwidth=0)
start2.configure(background='#588e84',activebackground='#54958a',borderwidth=0)

start1.place(relx=0.25,rely=0.7,anchor='n',relheight=0.1,relwidth=0.1)
start2.place(relx=0.75,rely=0.7,anchor='n',relheight=0.1,relwidth=0.1)

#key component
key=Entry(root,width=50,background='#4d5753',foreground='#96cdc9')
key.place(relx=0.5,rely=0.9,anchor='n',relwidth=0.4)

key.insert(0,'Type your cripto key here')

#random photo
img1=ImageTk.PhotoImage(Image.open('photos/criptologo2.png'))
lab1_=Label(image=img1)
lab1_.place(relx=0,rely=0,anchor='nw',relheight=0.15,relwidth=0.15)

root.mainloop()
