from tkinter import *

root = Tk()

w = Label(root, text="Additive:")
w.grid(row = 0,sticky=E)
w = Label(root, text="Subtractive:")
w.grid(row = 1, sticky=E)

w = Label(root, text="Red", bg="red", fg="white", height=2)
w.grid(row=0, column=1)

w = Label(root, text="Magenta", bg="magenta", fg="white")
w.grid(row=1, column=2)

w = Label(root, text="Cyan", bg="cyan", height=2)
w.grid(row=1, column=1)
w = Label(root, text="Magenta", bg="magenta", fg="white")
w.grid(row=1, column=2)
w = Label(root, text="Yellow", bg="yellow", height=2)
w.grid(row=1, column=3)

w = Label(root, text="Red", bg="red", fg="white", height=2)
w.grid(row=0, column=1)
w = Label(root, text="Green", bg="green", height=3)
w.grid(row=0, column=2)
w = Label(root, text="Blue", bg="blue", fg="white")
w.grid(row=0, column=3)

mainloop()
