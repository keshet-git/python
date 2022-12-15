from tkinter import *

window = Tk()

entry = Entry(window,
        font=('Arial', 50))
entry.pack(side=LEFT)

submit_button = Button(window,text='aubbmit', command=submit)
submit_button.pack(side=RIGHT)

window.mainloop()