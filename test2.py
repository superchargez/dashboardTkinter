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
lableCurrent.grid(row=0, column=1, columnspan=2)
lableLM = Label(root, text="Last Month", bg="yellow")
lableLM.grid(row=0, column=3, columnspan=2)
lableLY = Label(root, text="Last Year", bg="yellow")
lableLY.grid(row=0, column=5, columnspan=2)
lableTarget = Label(root, text="Target", bg="yellow")
lableTarget.grid(row=0, column=7, columnspan=2)


# row labels
lableNorth = Label(root, text="North", bg="pink")
lableNorth.grid(row=1, column=0, sticky='w', rowspan=1)
lableSouth = Label(root, text="South", bg="pink")
lableSouth.grid(row=2, column=0, sticky='w', rowspan=1)
lableCentral = Label(root, text="Central", bg="pink")
lableCentral.grid(row=3, column=0, sticky='w', rowspan=1)
lableNational = Label(root, text="NATIONAL", bg="pink")
lableNational.grid(row=4, column=0, sticky='w', rowspan=1)

def arrowDenied(value=-0):
    if value < -0.5:
        arrow = ImageTk.PhotoImage(Image.open(greenDown))
    elif value > 0.5:
        arrow = ImageTk.PhotoImage(Image.open(redUp))
    else: arrow = ImageTk.PhotoImage(Image.open(grayArrow))
    return arrow

# Arrows row 1
myimg = arrowDenied(tabel.loc[0][1])
panel11 = tk.Label(root, image = myimg)
# panel11.grid(row=1, column=1)
panel11t = tk.Label(root, text = tabel.loc[0][1])
panel11t.grid(row=1, column=2)

myimg1 = arrowDenied(tabel.loc[0][2])
panel12 = tk.Label(root, image = myimg1)
panel12.grid(row=1, column=3)
panel12t = tk.Label(root, text = tabel.loc[0][2] )
panel12t.grid(row=1, column=4)

myimg2 = arrowDenied(tabel.loc[0][3])
panel13 = tk.Label(root, image = myimg2)
panel13.grid(row=1, column=5)
panel13t = tk.Label(root, text = tabel.loc[0][3])
panel13t.grid(row=1, column=6)

myimg3 = arrowDenied(tabel.loc[0][4])
panel14 = tk.Label(root, image = myimg3)
panel14.grid(row=1, column=7)
panel14t = tk.Label(root, text=tabel.loc[0][4])
panel14t.grid(row=1, column=8)

# Arrows row 2
myimg4 = arrowDenied(tabel.loc[1][1])
panel15 = tk.Label(root, image = myimg4)
# panel15.grid(row=2, column=1)
panel15t = tk.Label(root, text = tabel.loc[1][1])
panel15t.grid(row=2, column=2)

myimg5 = arrowDenied(tabel.loc[1][2])
panel13 = tk.Label(root, image = myimg5)
panel13.grid(row=2, column=3)
panel13t = tk.Label(root, text = tabel.loc[1][2])
panel13t.grid(row=2, column=4)

myimg6 = arrowDenied(tabel.loc[1][3])
panel14 = tk.Label(root, image = myimg6)
panel14.grid(row=2, column=5)
panel14t = tk.Label(root, text = tabel.loc[1][3])
panel14t.grid(row=2, column=6)

myimg7 = arrowDenied(tabel.loc[1][4])
panel15 = tk.Label(root, image = myimg7)
panel15.grid(row=2, column=7)
panel15t = tk.Label(root, text=tabel.loc[1][4])
panel15t.grid(row=2, column=8)

# Arrows row 3
myimg8 = arrowDenied(tabel.loc[2][1])
panel16 = tk.Label(root, image = myimg8)
# panel16.grid(row=3, column=1)
panel16t = tk.Label(root, text = tabel.loc[2][1])
panel16t.grid(row=3, column=2)

myimg9 = arrowDenied(tabel.loc[2][2])
panel17 = tk.Label(root, image = myimg9)
panel17.grid(row=3, column=3)
panel17t = tk.Label(root, text = tabel.loc[2][2])
panel17t.grid(row=3, column=4)

myimg10 = arrowDenied(tabel.loc[2][3])
panel18 = tk.Label(root, image = myimg10)
panel18.grid(row=3, column=5)
panel18t = tk.Label(root, text = tabel.loc[2][3])
panel18t.grid(row=3, column=6)

myimg11 = arrowDenied(tabel.loc[2][4])
panel19 = tk.Label(root, image = myimg11)
panel19.grid(row=3, column=7)
panel19t = tk.Label(root, text=tabel.loc[2][4])
panel19t.grid(row=3, column=8)

# Arrows row 4
myimg12 = arrowDenied(tabel.loc[3][1])
panel20 = tk.Label(root, image = myimg12)
# panel20.grid(row=4, column=1)
panel20t = tk.Label(root, text = tabel.loc[3][1])
panel20t.grid(row=4, column=2)

myimg13 = arrowDenied(tabel.loc[3][2])
panel21 = tk.Label(root, image = myimg13)
panel21.grid(row=4, column=3)
panel21t = tk.Label(root, text = tabel.loc[3][2])
panel21t.grid(row=4, column=4)

myimg14 = arrowDenied(tabel.loc[3][3])
panel22 = tk.Label(root, image = myimg14)
panel22.grid(row=4, column=5)
panel22t = tk.Label(root, text = tabel.loc[3][3])
panel22t.grid(row=4, column=6)

myimg15 = arrowDenied(tabel.loc[3][4])
panel23 = tk.Label(root, image = myimg15)
panel23.grid(row=4, column=7)
panel23t = tk.Label(root, text=tabel.loc[3][4])
panel23t.grid(row=4, column=8)

root.mainloop()