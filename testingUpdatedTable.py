import os, sys, tkcap
from tkinter import *
import pandas as pd
import openpyxl as xl

path_to_excel = r"testdata.xlsx"
wb = wb = xl.load_workbook(path_to_excel)
sheets = wb.sheetnames
for i in sheets:
    dfs = [pd.read_excel(path_to_excel, sheet_name=i, skiprows=0) for i in sheets]

root = Tk()
redDown = PhotoImage(file="arrows/small-red-down.png")
redUp = PhotoImage(file="arrows/small-red-up.png")
greenDown =PhotoImage(file="arrows/small-green-down.png")
greenUp = PhotoImage(file="arrows/small-green-up.png")
grayArrow = PhotoImage(file="arrows/small-gray-right.png")
def redDownf(value=0):
    return redDown if value < -0.5 else greenUp if value > 0.5 else grayArrow
def greenDownf(value=0):
    return greenDown if value < -0.5 else redUp if value > 0.5 else grayArrow
root.title("KPI Dashboard")
products = ['xDSL', 'FF', 'Voice', 'IPTV']
calls = ['DENIED', "REGISTER", "REPEAT", "MTTR"]
colours = ["powder blue", 'bisque', "RosyBrown1", "khaki2", "light sea green"]
cursor = ['circle red', 'sizing red', 'target red', 'exchange red']
rows, columns = ['North', 'South', 'Central', 'National'], ['Current', 'Last Month', 'Last Year', 'Target']
counter = 0
frames = []
for i in range(4):
    for j in range(4):
        frame = LabelFrame(root, width=270, height=130, text = products[j],
        bg=colours[j], relief=RAISED, borderwidth=5, cursor="circle red")
        frames.append(frame)
        frame.grid(row=i,column=j, sticky="EW")
        
        Label(frames[counter], font=('Times New Roman', 8, 'bold'), text=calls[i], relief=RAISED,
        # bg=colours[j],
        bg="sky blue",
        borderwidth=2, cursor=cursor[i]).grid(row=0,column=0, sticky="EW")
        # Label(frames[counter], image=greenDown(), borderwidth=5, bg=colours[j], cursor=cursor[i]).grid(row=i+1,column=j*2+2, sticky="EW")
        for k in range(4):
            Label(frames[counter], text=columns[k],
            # bg=colours[j],
            bg="light yellow",
            relief=RAISED, borderwidth=2, cursor=cursor[i], width=10).grid(row=0,column=k+1, sticky="EW", columnspan=1)
            Label(frames[counter], text=rows[k], borderwidth=2,
            # bg=colours[j],
            bg="light pink",
            relief=RAISED, cursor=cursor[i], width=8).grid(row=k+1,column=0, sticky="EW", columnspan=1)
            print(i, j, k, counter)
            data = dfs[i].set_index('Region')
            value = data.iloc[j][k]
            Label(frames[i], text=value, background=colours[k]).grid(row=j+1, column=k*1+1, sticky='e')
            myimg1 = greenDownf(value)
            if k == 0: continue
            Label(frames[i], image=myimg1, bg=colours[k]).grid(row=j+1, column=k*1+1, sticky='w')
        counter+=1
root.mainloop()
