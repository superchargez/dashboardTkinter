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
root.option_add("*Label*sticky", 'ew')

# create columns
def createColumns(frameName):
    """ This create columns to be displayed"""
    lableCurrent = Label(frameName, text="Current", bg="yellow", borderwidth=5)
    lableCurrent.grid(row=0, column=1, columnspan=2)
    lableLM = Label(frameName, text="Last Month", bg="yellow", borderwidth=5)
    lableLM.grid(row=0, column=3, columnspan=2)
    lableLY = Label(frameName, text="Last Year", bg="yellow", borderwidth=5)
    lableLY.grid(row=0, column=5, columnspan=2)
    lableTarget = Label(frameName, text="Target", bg="yellow", borderwidth=5)
    lableTarget.grid(row=0, column=7, columnspan=2)
createColumns(root)
# row labels
def createRows(frameName):
    lableNorth = Label(frameName, text="North", bg="pink")
    lableNorth.grid(row=1, column=0, sticky='ew', rowspan=1)
    lableSouth = Label(frameName, text="South", bg="pink")
    lableSouth.grid(row=2, column=0, sticky='ew', rowspan=1)
    lableCentral = Label(frameName, text="Central", bg="pink")
    lableCentral.grid(row=3, column=0, sticky='we', rowspan=1)
    lableNational = Label(frameName, text="NATIONAL", bg="pink")
    lableNational.grid(row=4, column=0, sticky='we', rowspan=1)
createRows(root)

def arrowDenied(value=-0):
    if value < -0.5:
        arrow = ImageTk.PhotoImage(Image.open(greenDown))
    elif value > 0.5:
        arrow = ImageTk.PhotoImage(Image.open(redUp))
    else: arrow = ImageTk.PhotoImage(Image.open(grayArrow))
    return arrow

def ArrowsRecord(frameName, tabelName):
    """ Here we create values and arrows of table"""
    # Arrows row 1
    myimg = arrowDenied(tabelName.loc[0][1])
    panel11 = tk.Label(frameName, image = myimg)
    # panel11.grid(row=1, column=1)
    panel11t = tk.Label(frameName, text = tabelName.loc[0][1],borderwidth=1, relief='raised')
    panel11t.grid(row=1, column=2)

    myimg1 = arrowDenied(tabelName.loc[0][2])
    panel12 = tk.Label(frameName, image = myimg1)
    panel12.grid(row=1, column=3)
    panel12t = tk.Label(frameName, text = tabelName.loc[0][2], borderwidth=1, relief='raised')
    panel12t.grid(row=1, column=4)

    myimg2 = arrowDenied(tabelName.loc[0][3])
    panel13 = tk.Label(frameName, image = myimg2)
    panel13.grid(row=1, column=5)
    panel13t = tk.Label(frameName, text = tabelName.loc[0][3],borderwidth=1, relief='raised')
    panel13t.grid(row=1, column=6)

    myimg3 = arrowDenied(tabelName.loc[0][4])
    panel14 = tk.Label(frameName, image = myimg3)
    panel14.grid(row=1, column=7)
    panel14t = tk.Label(frameName, text=tabelName.loc[0][4],borderwidth=1, relief='raised')
    panel14t.grid(row=1, column=8)

    # Arrows row 2
    myimg4 = arrowDenied(tabelName.loc[1][1])
    panel15 = tk.Label(frameName, image = myimg4)
    # panel15.grid(row=2, column=1)
    panel15t = tk.Label(frameName, text = tabelName.loc[1][1],borderwidth=1, relief='raised')
    panel15t.grid(row=2, column=2)

    myimg5 = arrowDenied(tabelName.loc[1][2])
    panel13 = tk.Label(frameName, image = myimg5)
    panel13.grid(row=2, column=3)
    panel13t = tk.Label(frameName, text = tabelName.loc[1][2],borderwidth=1, relief='raised')
    panel13t.grid(row=2, column=4)

    myimg6 = arrowDenied(tabelName.loc[1][3])
    panel14 = tk.Label(frameName, image = myimg6)
    panel14.grid(row=2, column=5)
    panel14t = tk.Label(frameName, text = tabelName.loc[1][3],borderwidth=1, relief='raised')
    panel14t.grid(row=2, column=6)

    myimg7 = arrowDenied(tabelName.loc[1][4])
    panel15 = tk.Label(frameName, image = myimg7)
    panel15.grid(row=2, column=7)
    panel15t = tk.Label(frameName, text=tabelName.loc[1][4],borderwidth=1, relief='raised')
    panel15t.grid(row=2, column=8)

    # Arrows row 3
    myimg8 = arrowDenied(tabelName.loc[2][1])
    panel16 = tk.Label(frameName, image = myimg8)
    # panel16.grid(row=3, column=1)
    panel16t = tk.Label(frameName, text = tabelName.loc[2][1],borderwidth=1, relief='raised')
    panel16t.grid(row=3, column=2)

    myimg9 = arrowDenied(tabelName.loc[2][2])
    panel17 = tk.Label(frameName, image = myimg9)
    panel17.grid(row=3, column=3)
    panel17t = tk.Label(frameName, text = tabelName.loc[2][2],borderwidth=1, relief='raised')
    panel17t.grid(row=3, column=4)

    myimg10 = arrowDenied(tabelName.loc[2][3])
    panel18 = tk.Label(frameName, image = myimg10)
    panel18.grid(row=3, column=5)
    panel18t = tk.Label(frameName, text = tabelName.loc[2][3],borderwidth=1, relief='raised')
    panel18t.grid(row=3, column=6)

    myimg11 = arrowDenied(tabelName.loc[2][4])
    panel19 = tk.Label(frameName, image = myimg11)
    panel19.grid(row=3, column=7)
    panel19t = tk.Label(frameName, text=tabelName.loc[2][4],borderwidth=1, relief='raised')
    panel19t.grid(row=3, column=8)

    # Arrows row 4
    myimg12 = arrowDenied(tabelName.loc[3][1])
    panel20 = tk.Label(frameName, image = myimg12)
    # panel20.grid(row=4, column=1)
    panel20t = tk.Label(frameName, text = tabelName.loc[3][1],borderwidth=1, relief='raised')
    panel20t.grid(row=4, column=2)

    myimg13 = arrowDenied(tabelName.loc[3][2])
    panel21 = tk.Label(frameName, image = myimg13)
    panel21.grid(row=4, column=3)
    panel21t = tk.Label(frameName, text = tabelName.loc[3][2],borderwidth=1, relief='raised')
    panel21t.grid(row=4, column=4)

    myimg14 = arrowDenied(tabelName.loc[3][3])
    panel22 = tk.Label(frameName, image = myimg14)
    panel22.grid(row=4, column=5)
    panel22t = tk.Label(frameName, text = tabelName.loc[3][3],borderwidth=1, relief='raised')
    panel22t.grid(row=4, column=6)

    myimg15 = arrowDenied(tabelName.loc[3][4])
    panel23 = tk.Label(frameName, image = myimg15)
    panel23.grid(row=4, column=7)
    panel23t = tk.Label(frameName, text=tabelName.loc[3][4],borderwidth=1, relief='raised')
    panel23t.grid(row=4, column=8)

ArrowsRecord(root, tabel)
root.mainloop()
