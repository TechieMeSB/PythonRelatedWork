from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window=Tk()                           #create tkinter window
window.title("QR Code Generator")
window.configure(bg="#BFBABA")


def generate():                       #code generator
    if len(subject.get())!=0:
        global myQr,photo
        myQr=pyqrcode.create(subject.get())
        qrImage=myQr.xbm(scale=6)
        photo=BitmapImage(data=qrImage)
    else:
        messagebox.showinfo("Error!","Please Enter Subject")
    try:
        showCode()
    except:
        pass

def showCode():                       #shows the code
    global photo
    notificationLabel.config(image=photo)
    subLabel.config(text="Showing QR Code for:"+subject.get())

def save():
    dir =path1=os.getcwd()+"\\QR_Code"  #folder to save codes
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qrImage=myQr.png(os.path.join(dir,name.get()+".png"),scale=6)
        else:
            messagebox.showinfo("Error!","File name can not be empty!")
    except:
        messagebox.showinfo("Error!","Please generate code 1st")


lab1=Label(window,text="Enter Subject",font=("Helvetica",12))
lab1.grid(row=0,column=0,sticky=N+S+E+W)

lab2=Label(window,text="Enter File name",font=("Helvetica",12))
lab2.grid(row=1,column=0,sticky=N+S+E+W)

subject=StringVar()
subjectEntry=Entry(window,textvariable=subject,font=("Helvetica",12))
subjectEntry.grid(row=0,column=1,sticky=N+S+E+W)

name=StringVar()
nameEntry=Entry(window,textvariable=name,font=("Helvetica",12))
nameEntry.grid(row=1,column=1,sticky=N+S+E+W)

createButton=Button(window,text="CREATE QR CODE",bg="#59B5EF",font=("Helvetica",12),width=15,command=generate)
createButton.grid(row=0,column=3,stick=N+S+E+W)

notificationLabel=Label(window)
notificationLabel.grid(row=2,column=1,sticky=N+S+E+W)

subLabel=Label(window,text="",bg="#BFBABA")
subLabel.grid(row=3,column=1,sticky=N+S+E+W)

showButton=Button(window,text="Save as PNG",bg="#0F6FD8",font=("Helvetica",12),width=15,command=save)
showButton.grid(row=1,column=3,sticky=N+S+E+W)

#Making Responsive layout
totalRows=3
totalCols=3
for row in range(totalRows+1):
    window.grid_rowconfigure(row,weight=1)

for col in range(totalCols+1):
    window.grid_columnconfigure(col,weight=1)

#looping the GUI
window.mainloop()
