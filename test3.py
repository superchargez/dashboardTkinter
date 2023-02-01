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

redDown = r"arrows/small-red-down.png"
redUp = r"arrows/small-red-up.png"
greenDown = r"arrows/small-green-down.png"
greenUp = r"arrows/small-green-up.png"
grayArrow = r"arrows/small-gray-right.png"

def arrowDenied(value=-0):
    if value < -0.5:
        arrow = ImageTk.PhotoImage(Image.open(greenDown))
    elif value > 0.5:
        arrow = ImageTk.PhotoImage(Image.open(redUp))
    else: arrow = ImageTk.PhotoImage(Image.open(grayArrow))
    return arrow

for i in range(4):
    counter 	= 0
    for j in range(4):
        label = tk.Label(root, text=tabel.iloc[i][j]).grid(row=i,column=counter, sticky='news')
        counter+=1
        myimg1 = arrowDenied(tabel.iloc[i][j])
        panel12 = tk.Label(root, image = myimg1).grid(row=i, column=counter)
        counter+=1
        

root.mainloop()
