# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:02:58 2020

@author: srish
"""

import json,requests
from tkinter import *

window=Tk()
window.title("Covid-19")
window.configure(bg="#CEEFF2")

window.geometry('400x100')

lbl=Label(window,text="Total Active cases         ::-....",bg="#CEEFF2")
lbl1=Label(window,text="Total Confirmed cases ::-....",bg="#CEEFF2")

lbl.grid(column=1, row=0)
lbl1.grid(column=1, row=1)
lbl2=Label(window,text="",bg="#CEEFF2")
lbl2.grid(column=1,row=3)

def click():
    try:
        url="https://api.covid19india.org/data.json"
        page=requests.get(url)
        data=json.loads(page.text)
        lbl.configure(text="Total active cases:-" + data["statewise"][0]["active"])
        lbl1.configure(text="Total confirmed cases:-" + data["statewise"][0]["confirmed"])
        lbl2.configure(tet="Data Refreshed")
    except:
        pass

btn=Button(window,text="Refresh",command=click,bg="#0CC4DB")
btn.grid(column=2,row=3)

window.mainloop()
