import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

redDown = r"arrows/red down.png"
greenUp = r"arrows/green up.png"

LM = 10

root = tk.Tk()
lableT = Label(root, text="green down arrow", bg="green")
lableT.grid(row=0, column=0)

def cond():
    if LM < 0:
        imgage = ImageTk.PhotoImage(Image.open(redDown))
    else: imgage = ImageTk.PhotoImage(Image.open(greenUp))
    return imgage



img = cond()
panel = tk.Label(root, image = img)

panel.grid(row=0, column=1)
panel.config(bg="green", width=300, height=300)

# myCanvas = Canvas(panel, width=180, height=200)
# myCanvas.grid(row=0, column=1)
# img = ImageTk.PhotoImage(Image.open(greenDown))

root.mainloop()
