from tkinter import *

root = Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Label(root, text="")
        print(b);
        b.grid(row=i, column=j)

mainloop()
