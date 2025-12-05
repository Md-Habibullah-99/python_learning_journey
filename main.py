
from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="I am Habibullah")
myLabel3 = Label(root, text="Studying in CSE")
# Shoving it onto the screen

myLabel1.grid(row=0,column=2)
myLabel2.grid(row=1,column=18)
myLabel3.grid(row=5,column=10)


root.mainloop()


