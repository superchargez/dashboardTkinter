from tkinter import *
root = Tk()
counter = 0
frames = []
for i in range(4):
    for j in range(4):
        frame = LabelFrame(root, width=270, height=130, text = "_".join(["product", str(j)]))
        frames.append(frame)
        frame.grid(row=i,column=j, sticky="EW")
        Label(frames[counter], text="_".join(["Calls",str(j)])).grid(row=0,column=0, sticky="EW")
        for k in range(4):
            Label(frames[counter], text="".join(["column ",str(k+1)])).grid(row=0,column=k*2+1, sticky="EW", columnspan=2)
            Label(frames[counter], text="".join(["row ", str(k+1)])).grid(row=k+1,column=0, sticky="EW", columnspan=1)
            Label(frames[i], text="r"+str(j)+"c"+str(k)).grid(row=j+1, column=k*2+1, sticky='e')
            if i == 0: continue
            Label(frames[i], text="p =>"+str(counter)).grid(row=j+1, column=k*1+2, sticky='w')
        counter+=1
root.mainloop()
