import tkinter as tk
from tkinter import ttk
from tkinter import *

def btnClickFunction():
    print("klik")

root = Tk()

root.geometry('1920x1080')
root.configure(background='#050505')
root.title('titlebar')

Button(root, text='knopje', bg='#00FFFF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=20, y=20)
Label()





root.mainloop()