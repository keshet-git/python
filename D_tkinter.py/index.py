from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Look i clicked a button')
    myLabel.pack()

myButton = Button(root, text='bee myn', command=myClick, fg='blue', bg='#ffffff')
myButton.pack()


root.mainloop()