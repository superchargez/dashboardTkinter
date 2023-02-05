import os, sys, tkcap
from tkinter import *
import pandas as pd
import openpyxl as xl

path_to_excel = r"testdata.xlsx"
wb = wb = xl.load_workbook(path_to_excel)
sheets = wb.sheetnames
# for i in sheets:
#     dfs = [pd.read_excel(path_to_excel, sheet_name=i, skiprows=0) for i in sheets]

root = Tk()
root.config(padx=10, pady=10)
root.title("KPI Dashboard")
products = ['xDSL', 'FF', 'Voice', 'IPTV']
colours = ["powder blue", 'bisque', "RosyBrown1", "khaki2"]
counter = 0
frames = []
for i in range(4):
    for j in range(4):
        frames.append({''.join(["frame",str(i),str(j)]):LabelFrame(root, width=270, height=130, text = products[j],
            # bg="light sea green",
            bg=colours[j],
            relief=RAISED, borderwidth=5,
            cursor="circle red").grid(row=i,column=j, sticky="EW")})

        counter+=1
print(type(frames[0]))
root.mainloop()
