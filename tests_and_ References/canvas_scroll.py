from tkinter import Tk, Frame, Canvas, Scrollbar, HORIZONTAL, VERTICAL, Label, \
     PhotoImage

from PIL import Image, ImageTk


root=Tk()

frame=Frame(root,width=500,height=100)
frame.grid(row=0,column=0)

#img = PhotoImage(file = '/home/raja/Pictures/Python_vs._others.png');
image = Image.open("/home/raja/Pictures/facebook/FB_IMG_14625555879653356.jpg");
photo = ImageTk.PhotoImage(image)
canvas=Canvas(frame,bg='violet',width=800,height=500,scrollregion=(0,0,900,800));
canvas.create_image(300, 300, image = photo)

hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.grid(row = 1, column = 0, sticky = 'ew');
hbar.config(command=canvas.xview)

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.grid(row = 0, column = 1, sticky = 'ns');
vbar.config(command=canvas.yview)

##canvas.config(width=300,height=300)
canvas.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)
canvas.grid(row = 0, column = 0, sticky = 'nsew');

l = Label(frame, bg = 'red').grid(row = 0, column = 2 , sticky = 'nsew');

root.mainloop()

