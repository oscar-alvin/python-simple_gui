#!/usr/bin/python
import tkinter
import tkinter.messagebox
from tkinter import *

top = tkinter.Tk()
top = Label(None, text='PROGRAM PYTHON PERTAMA SAYA')
top.pack(side=TOP)
top = Label(None, text='Nama')
top.pack(side=LEFT)
entriNama = Entry(None)
entriNama.pack(side=LEFT)
top = Label(None, text='NIM')
top.pack(side=LEFT)
entriNim = Entry(None)
entriNim.pack(side=LEFT)

def ambilValue():
	gabung = entriNama.get() +" "+entriNim.get()
	messagebox.showinfo( "Hello Python", gabung)
top = Button(None, text='Click Me', command=ambilValue)
top.pack(side=BOTTOM)
top.mainloop()
