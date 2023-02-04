import os, sys
import tkinter as tk
import pandas as pd
import tkcap
import openpyxl as xl

def load_excel(path_to_excel):
	if not os.path.isfile(path_to_excel):
		print('File is not found.')
		sys.exit()
	else:
		wb = xl.load_workbook(path_to_excel)
		sheet_names = wb.get_sheet_names()
		sheet = wb[sheet_names[0]]
		df = pd.read_excel(path_to_excel, sheet_name=sheet_names[0])
		return df

root = tk.Tk()
root.config(padx=10, pady=10)
root.title("KPI Dashboard")
def frameMaker(colour, product, r, c):
    """ This will create simple frames"""
    frame = tk.LabelFrame(root, width=270, height=130, text = product,
            bg=colour, relief=tk.RAISED, borderwidth=5, cursor="dot").grid(row=r, column=c)
    return frame
cursors =[
        "arrow",
        "circle",
        "clock",
        "cross",
        "dotbox",
        "exchange",
        "fleur",
        "heart",
        "man",
        "mouse",
        "pirate",
        "plus",
        "shuttle",
        "sizing",
        "spider",
        "spraycan",
        "star",
        "target",
        "tcross",
        "trek"
]
#####
frame1 = tk.LabelFrame(root, width=270, height=130, text = 'XDSL',
            # bg="light sea green",
            bg="powder blue",
            relief=tk.RAISED, borderwidth=5, 
            cursor="circle red")
frame1.grid(row=0,column=0, sticky="EW")

frame2 = tk.LabelFrame(root, width=270, height=130, text = 'FF',
            bg="bisque",
            relief=tk.RAISED, borderwidth=5, 
            cursor="target green")
frame2.grid(row=0,column=1, sticky="EW")

frame3 = tk.LabelFrame(root, width=270, height=130, text = 'Voice',
            bg="RosyBrown1",
            # bg="black",
            relief=tk.RAISED, borderwidth=5, 
            cursor="tcross")
frame3.grid(row=0,column=2, sticky="EW")

frame4 = tk.LabelFrame(root, width=270, height=130, text = 'IPTV',
            bg="khaki2",
            relief=tk.RAISED, borderwidth=5,
            cursor="dot blue")
frame4.grid(row=0,column=3, sticky="EW")
tk.Label(frame1, text="DENIED").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame2, text="DENIED").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame3, text="DENIED").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame4, text="DENIED").grid(row=0,column=0, sticky="NEWS")
#######
frame5 = tk.LabelFrame(root, width=270, height=130, text = 'XDSL',
            bg="powder blue",
            relief=tk.RAISED, borderwidth=5, 
            cursor="dot")
frame5.grid(row=1,column=0, sticky="NEWS")

frame6 = tk.LabelFrame(root, width=270, height=130, text = 'FF',
            bg="bisque",
            relief=tk.RAISED, borderwidth=5, 
            cursor="arrow")
frame6.grid(row=1,column=1, sticky="NEWS")

frame7 = tk.LabelFrame(root, width=270, height=130, text = 'Voice',
            bg="RosyBrown1",
            # bg="black",
            relief=tk.RAISED, borderwidth=5, 
            cursor="dot")
frame7.grid(row=1,column=2, sticky="NEWS")

frame8 = tk.LabelFrame(root, width=270, height=130, text = 'IPTV',
            bg="khaki2",
            relief=tk.RAISED, borderwidth=5,
            cursor="arrow")
frame8.grid(row=1,column=3, sticky="NEWS")
tk.Label(frame5, text="Reg").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame6, text="Reg").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame7, text="Reg").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame8, text="Reg").grid(row=0,column=0, sticky="NEWS")
#######
frame9 = tk.LabelFrame(root, width=270, height=130, text = 'XDSL',
            bg="powder blue",
            relief=tk.RAISED, borderwidth=5, 
            cursor="dot")
frame9.grid(row=2,column=0, sticky='NEWS')

frame10 = tk.LabelFrame(root, width=270, height=130, text = 'FF',
            bg="bisque",
            relief=tk.RAISED, borderwidth=5, 
            cursor="arrow")
frame10.grid(row=2,column=1, sticky="NEWS")

frame11 = tk.LabelFrame(root, width=270, height=130, text = 'Voice',
            bg="RosyBrown1",
            # bg="black",
            relief=tk.RAISED, borderwidth=5, 
            cursor="dot")
frame11.grid(row=2,column=2, sticky="NEWS")

frame12 = tk.LabelFrame(root, width=270, height=130, text = 'IPTV',
            bg="khaki2",
            relief=tk.RAISED, borderwidth=5,
            cursor="arrow")
frame12.grid(row=2,column=3, sticky="NEWS")
tk.Label(frame9, text="Repeat").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame10, text="Repeat").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame11, text="Repeat").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame12, text="Repeat").grid(row=0,column=0, sticky="NEWS")
#######
frame13 = tk.LabelFrame(root, width=270, height=130, text = 'XDSL',
            bg="powder blue",
            relief=tk.RAISED, borderwidth=5, 
            cursor="dot")
frame13.grid(row=3,column=0)

frame14 = tk.LabelFrame(root, width=270, height=130, text = 'FF',
            bg="bisque",
            relief=tk.RAISED, borderwidth=5, 
            cursor="arrow")
frame14.grid(row=3,column=1)

frame15 = tk.LabelFrame(root, width=270, height=130, text = 'Voice',
            bg="RosyBrown1",
            # bg="black",
            relief=tk.RAISED, borderwidth=5, 
            cursor="dot")
frame15.grid(row=3,column=2)

frame16 = tk.LabelFrame(root, width=270, height=130, text = 'IPTV',
            bg="khaki2",
            relief=tk.RAISED, borderwidth=5,
            cursor="arrow")
frame16.grid(row=3,column=3)
tk.Label(frame13, text="MTTR").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame14, text="MTTR").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame15, text="MTTR").grid(row=0,column=0, sticky="NEWS")
tk.Label(frame16, text="MTTR").grid(row=0,column=0, sticky="NEWS")
#####
redDown = tk.PhotoImage(file="arrows/small-red-down.png")
redUp = tk.PhotoImage(file="arrows/small-red-up.png")
greenDown = tk.PhotoImage(file="arrows/small-green-down.png")
greenUp = tk.PhotoImage(file="arrows/small-green-up.png")
grayArrow = tk.PhotoImage(file="arrows/small-gray-right.png")

xDSLdeniedMain = pd.read_excel('testdata.xlsx', sheet_name='xdsldenied', index_col='Region')
FFdeniedMain = pd.read_excel('testdata.xlsx', sheet_name='ffdenied', index_col='Region')
VoicedeniedMain = pd.read_excel('testdata.xlsx', sheet_name='voicedenied', index_col='Region')
IPTVdeniedMain = pd.read_excel('testdata.xlsx', sheet_name='iptvdenied', index_col='Region')
xDSLregMain = pd.read_excel('testdata.xlsx', sheet_name='xdslreg', index_col='Region')
FFregMain = pd.read_excel('testdata.xlsx', sheet_name='ffreg', index_col='Region')
VoiceregMain = pd.read_excel('testdata.xlsx', sheet_name='voicereg', index_col='Region')
IPTVregMain = pd.read_excel('testdata.xlsx', sheet_name='iptvreg', index_col='Region')
xDSLrepeatMain = pd.read_excel('testdata.xlsx', sheet_name='xdslrepeat', index_col='Region')
FFrepeatMain = pd.read_excel('testdata.xlsx', sheet_name='ffrepeat', index_col='Region')
VoicerepeatMain = pd.read_excel('testdata.xlsx', sheet_name='voicerepeat', index_col='Region')
IPTVrepeatMain = pd.read_excel('testdata.xlsx', sheet_name='iptvrepeat', index_col='Region')
xDSLMTTRMain = pd.read_excel('testdata.xlsx', sheet_name='xdslMTTR', index_col='Region')
FFMTTRMain = pd.read_excel('testdata.xlsx', sheet_name='ffMTTR', index_col='Region')
VoiceMTTRMain = pd.read_excel('testdata.xlsx', sheet_name='voiceMTTR', index_col='Region')
IPTVMTTRMain = pd.read_excel('testdata.xlsx', sheet_name='iptvMTTR', index_col='Region')

# deniedArrow = deniedMain.iloc[:,1:]

def arrowReg(value=0):
    return redDown if value < -0.5 else greenUp if value > 0.5 else grayArrow

def arrowDenied(value=0):
    return greenDown if value < -0.5 else redUp if value > 0.5 else grayArrow

def myRows(frameName, bgColour, table_):
    for i, txt in enumerate(table_.index.values):
        lbl = tk.Label(frameName, text=txt, bg=bgColour, width=10, bd=1, relief="raised")
        lbl.grid(row=i+1, column=0, sticky="news")
        
def myColumns(frameName, bgColour, table_):
    for i, col in enumerate(table_.columns.values):
        lbl = tk.Label(frameName, text=col, bg=bgColour, width=10, bd=1, relief="raised")
        lbl.grid(row=0, column=i*2+1, columnspan=2, sticky="news")
        
def myTabel(frameName, bgColour, table_):
    for i in range(4):
        for j in range(4):
            value = table_.iloc[i][j]
            tk.Label(frameName, text=value, background=bgColour).grid(row=i+1, column=j*2+1, sticky='e')
            if j == 0:
                continue
            if str(table_) == str("deniedMain"):
                myimg1 = arrowDenied(value)
            if str(table_) == str("regMain"):
                myimg1 = arrowReg(value)
            if str(table_) == str("repeatMain"):
                myimg1 = arrowDenied(value)
            else:myimg1 = arrowReg(value)
            tk.Label(frameName, image=myimg1, bg=bgColour).grid(row=i+1, column=j*2+2, sticky='w')

tabel = pd.read_excel('testdata.xlsx', sheet_name='xdsldenied', index_col='Region')
# Finally Add Rows
myRows(frame1, "pink", tabel)
myRows(frame2, "pink", tabel)
myRows(frame3, "pink", tabel)
myRows(frame4, "pink", tabel)
myRows(frame5, "pink", tabel)
myRows(frame6, "pink", tabel)
myRows(frame7, "pink", tabel)
myRows(frame8, "pink", tabel)
myRows(frame9, "pink", tabel)
myRows(frame10, "pink", tabel)
myRows(frame11, "pink", tabel)
myRows(frame12, "pink", tabel)
myRows(frame13, "pink", tabel)
myRows(frame14, "pink", tabel)
myRows(frame15, "pink", tabel)
myRows(frame16, "pink", tabel)
# Finally add columns
myColumns(frame1, 'beige', tabel)
myColumns(frame2, 'beige', tabel)
myColumns(frame3, 'beige', tabel)
myColumns(frame4, 'beige', tabel)
myColumns(frame5, 'beige', tabel)
myColumns(frame6, 'beige', tabel)
myColumns(frame6, 'beige', tabel)
myColumns(frame7, 'beige', tabel)
myColumns(frame8, 'beige', tabel)
myColumns(frame9, 'beige', tabel)
myColumns(frame10, 'beige', tabel)
myColumns(frame11, 'beige', tabel)
myColumns(frame12, 'beige', tabel)
myColumns(frame13, 'beige', tabel)
myColumns(frame14, 'beige', tabel)
myColumns(frame15, 'beige', tabel)
myColumns(frame16, 'beige', tabel)
#NOW FINALLY THE TABLES
myTabel(frame1, "powder blue", xDSLdeniedMain)
myTabel(frame2, "bisque", FFdeniedMain)
myTabel(frame3, "RosyBrown1", VoicedeniedMain)
myTabel(frame4, "khaki2", IPTVdeniedMain)
myTabel(frame5, "powder blue", xDSLregMain)
myTabel(frame6, "bisque", FFregMain)
myTabel(frame7, "RosyBrown1", VoiceregMain)
myTabel(frame8, "khaki2", IPTVregMain)
myTabel(frame9, "powder blue", xDSLrepeatMain)
myTabel(frame10, "bisque", FFrepeatMain)
myTabel(frame11, "RosyBrown1", VoicerepeatMain)
myTabel(frame12, "khaki2", IPTVrepeatMain)
myTabel(frame13, "powder blue", xDSLMTTRMain)
myTabel(frame14, "bisque", FFMTTRMain)
myTabel(frame15, "RosyBrown1", VoiceMTTRMain)
myTabel(frame16, "khaki2", IPTVMTTRMain)

def myColumns(frame, color, tabel):
    """this function creates columns on the Tkinter frame"""
    try:
        frame.columnconfigure(0, weight=1)
    except:
        pass
    for i in range(1, 16):
        try:
            frame.columnconfigure(i, weight=1)
        except:
            pass
        frame.grid_columnconfigure(i, weight=1)

# loopsave('mainloop.png')
def loopsaver3(filename):
    """ This function will check if the file name already exists, if image already exists then delete it if not it will create it"""
    try:
        tkcap.CAP(root).capture(filename)
    except tkcap.exceptions.ImageNameExistsError:
        # sys.exit("error in main loop")
        # print(f'image alreay exists')
        while True:
            choice = input("file already exists, do you want to overwrite (y/n): ")
            if choice == "y":
                os.remove(filename)
                # tkcap.CAP(root).capture(filename)
                break
            elif choice == "n":
                print("exiting..")
                break
            else:
                print("invalid input")
                continue

loopsaver3('mainloop.png')

root.mainloop()
