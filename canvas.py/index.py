from tkinter import *

root = Tk()
root.title('Codemy.com - Canvas')
#root.iconbitmap('.bee-icon.png')
root.geometry("700x700")


my_canvas = Canvas(root, width=700, height=700, bg="white")
my_canvas.pack(pady=20)

# Rectangle
#my_canvas.create_rectangle(x1, y1, x2, y2, fill="pink")
# Rectangle x1, y1: Top Left
# Rectangle x2, y2: Bottom Right

#my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")


#Create Oval
# Oval x1, y1: Top Left
# Oval x2, y2: Bottom Right
#my_canvas.create_oval(50, 100, 250, 50, fill="cyan")


# Create Line
# my_canvas.create_line(x1, y1, x2, y2, fill="color")
my_canvas.create_line(100, 100, 700, 100, fill="red")
my_canvas.create_line(0, 200, 600, 200, fill="red")
my_canvas.create_line(100, 300, 700, 300, fill="red")
my_canvas.create_line(0, 400, 600, 400, fill="red")
my_canvas.create_line(100, 500, 700, 500, fill="red")
my_canvas.create_line(0, 600, 700, 600, fill="red")

my_canvas.create_line(100, 100, 100, 200, fill="red") # ]
my_canvas.create_line(600, 200, 600, 300, fill="red") # ]

my_canvas.create_line(100, 300, 100, 400, fill="red") # ]
my_canvas.create_line(600, 400, 600, 500, fill="red") # ]

my_canvas.create_line(100, 500, 100, 600, fill="red") # ]

# my_canvas.create_line(300, 100, 300, 200, fill="red") # ]
# my_canvas.create_line(400, 100, 400, 200, fill="red") # ]



root.mainloop()