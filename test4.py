from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import pandas as pd
import numpy as np

tabel = pd.read_excel('testdata.xlsx', sheet_name='denied', index_col='Region')
print(tabel)
root = tk.Tk()
root.option_add("*Label*sticky", 'ew')

redDown = ImageTk.PhotoImage(Image.open(r"arrows/small-red-down.png"))
redUp = ImageTk.PhotoImage(Image.open(r"arrows/small-red-up.png"))
greenDown = ImageTk.PhotoImage(Image.open(r"arrows/small-green-down.png"))
greenUp = ImageTk.PhotoImage(Image.open(r"arrows/small-green-up.png"))
grayArrow = ImageTk.PhotoImage(Image.open(r"arrows/small-gray-right.png"))

def arrowDenied(value=-0):
    if value < -0.5:
        return greenDown
    elif value > 0.5:
        return redUp
    else: return grayArrow

for i in range(4):
    counter 	= 0
    for j in range(4):
        # print(f'TEXT-label is placed at {counter}')
        label = tk.Label(root, text=tabel.iloc[i][j]).grid(row=i,column=counter, sticky='e')
        counter+=1
        myimg1 = arrowDenied(tabel.iloc[i][j])
        # print(f'IMAGE-label is placed at {counter}')
        panel12 = tk.Label(root, image = myimg1).grid(row=i, column=counter, sticky='w')
        counter+=1
        
root.mainloop()
