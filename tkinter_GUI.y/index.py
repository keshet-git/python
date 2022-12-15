from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('my firsr GUI program')

icon = PhotoImage(file='chipmunk-icon.png')
window.iconphoto(True,icon)
window.config(background='#5cfcff')

window.mainloop()