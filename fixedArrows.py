import tkinter as tk
import pandas as pd

tabel = pd.read_excel('testdata.xlsx', sheet_name='denied', index_col='Region')
print(tabel)

root = tk.Tk()
root.config(padx=10, pady=10)

#redDown = tk.PhotoImage(file="arrows/small-red-down.png")
redUp = tk.PhotoImage(file="arrows/small-red-up.png")
greenDown = tk.PhotoImage(file="arrows/small-green-down.png")
#greenUp = tk.PhotoImage(file="arrows/small-green-up.png")
grayArrow = tk.PhotoImage(file="arrows/small-gray-right.png")

def arrowDenied(value=0):
    return greenDown if value < -0.5 else redUp if value > 0.5 else grayArrow

# row labels
for i, txt in enumerate(tabel.index.values):
    lbl = tk.Label(root, text=txt, bg="pink", width=10, bd=1, relief="raised")
    lbl.grid(row=i+1, column=0, sticky="nsew")

# column headings
for i, col in enumerate(tabel.columns.values):
    lbl = tk.Label(root, text=col, bg="yellow", width=10, bd=1, relief="raised")
    lbl.grid(row=0, column=i*2+1, columnspan=2, sticky="nsew")

for i in range(4):
    for j in range(4):
        value = tabel.iloc[i][j]
        tk.Label(root, text=value).grid(row=i+1, column=j*2+1, sticky='e')
        myimg1 = arrowDenied(value)
        tk.Label(root, image=myimg1).grid(row=i+1, column=j*2+2, sticky='w')

root.mainloop()