from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import pandas as pd
import numpy as np

tabel = pd.read_excel('testdata.xlsx', sheet_name='denied')
print(tabel)

redDown = r"arrows/small-red-down.png"
redUp = r"arrows/small-red-up.png"
greenDown = r"arrows/small-green-down.png"
greenUp = r"arrows/small-green-up.png"
grayArrow = r"arrows/small-gray-right.png"

root = tk.Tk()

# create columns
lableCurrent = Label(root, text="Current", bg="yellow")
lableCurrent.grid(row=0, column=1)
lableLM = Label(root, text="Last Month", bg="yellow")
lableLM.grid(row=0, column=2)
lableLY = Label(root, text="Last Year", bg="yellow")
lableLY.grid(row=0, column=3)
lableTarget = Label(root, text="Target", bg="yellow")
lableTarget.grid(row=0, column=4)


# row labels
lableNorth = Label(root, text="North", bg="pink")
lableNorth.grid(row=0+1, column=0, sticky='w')
lableSouth = Label(root, text="South", bg="pink")
lableSouth.grid(row=1+1, column=0, sticky='w')
lableCentral = Label(root, text="Central", bg="pink")
lableCentral.grid(row=2+1, column=0, sticky='w')
lableNational = Label(root, text="NATIONAL", bg="pink")
lableNational.grid(row=3+1, column=0, sticky='w')

def arrowDenied(value=-0):
    if value < -0.5:
        arrow = ImageTk.PhotoImage(Image.open(greenDown))
    elif value > 0.5:
        arrow = ImageTk.PhotoImage(Image.open(redUp))
    else: arrow = ImageTk.PhotoImage(Image.open(grayArrow))
    return arrow

myimg = arrowDenied(tabel.loc[0][2])
panel = tk.Label(root, image = myimg)
panel.grid(row=1, column=2)

root.mainloop()
