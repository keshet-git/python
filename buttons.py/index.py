from tkinter import *

root = Tk()
root.geometry('300x300')

l = Label(root, text='Bee my')
l.pack(side=LEFT)

def buttonFunction():
    print('Hello World')
#===============
photo = PhotoImage(file='bee-icon.png')

b = Button(root, text="click my",
                command=buttonFunction, 
                font=('comic Sans',30),
                fg='#00FF00',
                bg="black",
                activeforeground='#00FF00',
                activebackground='#00FF00',
                state=ACTIVE,
                image=photo
                )
b.pack(side=TOP)

#b2 = Button(root,text="click my", 
 #               command=buttonFunction, 
  #              font=('comic Sans',30),
   #             fg='#00FF00',
    #            bg="black",
     ##           activeforeground='#00FF00',
       #         activebackground='#00FF00',
        #        state=ACTIVE,
         #       image=photo
          #      )
#b2.pack(side=BOTTOM)

root.mainloop()