from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
import pandas as pd
import numpy as np

root = tk.Tk()

root.option_add("*Label*Font", ("Helvetica", 32))
root.option_add("*Label*Foreground", "white")
root.option_add("*Label*Background", "red")
root.option_add("*Label*padX", 5)
root.option_add("*Label*padY", 5)
root.option_add("*Label*sticky", 'ew')

root.title("KPI Dashboard")
frame = LabelFrame(root, width=270, height=130, text = 'XDSL',
            bg="light sea green",
            relief=RAISED, borderwidth=5, 
            cursor="dot")
frame.grid(row=0,column=0)

frame2 = LabelFrame(root, width=270, height=130, text = 'FF',
            bg="bisque",
            relief=RAISED, borderwidth=5, 
            cursor="arrow")
frame2.grid(row=0,column=1)

frame3 = LabelFrame(root, width=270, height=130, text = 'Voice',
            bg="RosyBrown1",
            relief=RAISED, borderwidth=5, 
            cursor="dot")
frame3.grid(row=0,column=2)

frame4 = LabelFrame(root, width=270, height=130, text = 'IPTV',
            bg="khaki2",
            relief=RAISED, borderwidth=5,
            cursor="arrow")
frame4.grid(row=0,column=3)


root.mainloop()
