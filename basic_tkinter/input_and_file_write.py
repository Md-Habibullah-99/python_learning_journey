
from tkinter import *
import os

root = Tk()

e = Entry(root, width=50, bg="gray")
e.pack()
e.insert(0)


def myClick():
    with open("usrData.txt","a") as f:
        f.write(f"{e.get()}\n")


myButton1 = Button(root, text="Click Me!", command=myClick, fg="white", bg="gray")
myButton1.pack()


root.mainloop()


