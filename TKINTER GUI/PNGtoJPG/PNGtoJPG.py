# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:20:32 2020

@author: srish
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image

root=tk.Tk()
root.title("PNG To JPG Converter")

canvas1=tk.Canvas(root,width=300,height=250,bg='azure3',relief='raised')
canvas1.pack()

label1=tk.Label(root,text='File Conversion Tool',bg='azure3')
label1.config(font=('helvetica',20))
canvas1.create_window(150,60,window=label1)

def getPNG():
    global img

    import_file_path= filedialog.askopenfilename()
    img=Image.open(import_file_path).convert('RGB')

browsePNG=tk.Button(root,text=" Import PNG File ",command=getPNG,bg='royalblue',fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,130,window=browsePNG)

def convertToJPG():
    global img
    export_file_path=filedialog.asksaveasfilename(defaultextension='.jpg')
    img.save(export_file_path)


saveAsJPG= tk.Button(root,text='Convert PNG to JPG',command=convertToJPG,bg='royalblue',fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,180,window=saveAsJPG)

root.mainloop()
