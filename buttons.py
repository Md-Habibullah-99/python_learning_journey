
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! It worked")
    myLabel.pack()

myButton1 = Button(root, text="Click Me!", command=myClick, fg="white",
                    bg="gray") # also i can use hex color code
myButton1.pack()

# DISABLED
myButton2 = Button(root, text="Click Me!", state=DISABLED)
myButton2.pack()

# padding
myButton3 = Button(root, text="Click Me!", padx=50, pady=100)
myButton3.pack()

#Destroy
destroy = Button(root, text="Close the window", padx=50, pady=50, command=root.destroy)
destroy.pack()

root.mainloop()


