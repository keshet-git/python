from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Yuor Name: ")

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text='Enter Your Stock Quore', command=myClick)
myButton.pack()

root.mainloop()