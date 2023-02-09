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
        Label(frames[counter], font=('Times New Roman', 8, 'bold'), text=calls[i], relief=RAISED, bg="sky blue", borderwidth=2, cursor=cursor[i]).grid(row=0,column=0, sticky="EW")
        for k in range(4):
            Label(frames[counter], text=counter, relief=RAISED, borderwidth=2, cursor=cursor[i], width=10, bg="light yellow").grid(row=0,column=k*2+1, sticky="EW", columnspan=2)
            Label(frames[counter], text=rows[k], borderwidth=2, pady=1, relief=RAISED, cursor=cursor[i], width=8, bg="light pink").grid(row=k+1,column=0, sticky="EW", columnspan=1)
            data = dfs[counter].set_index('Region')
            value = data.iloc[j][k]
            myimg1 = greenDownf(value)
            for m in range(4):
                Label(frames[counter], text=value,bg=colours[j]).grid(row=k+1,column=m*2+1, sticky="E", columnspan=1) # numbers in the table
                if m == 0: continue
                Label(frames[counter], fg = 'red', font="bold", bg=colours[j], image=myimg1).grid(row=k+1,column=m*2+2, sticky="W", columnspan=1) # numbers in the table
        counter+=1
root.mainloop()
