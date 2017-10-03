from tkinter import *
from PIL import Image, ImageTk


root = Tk()

canvas = Canvas(width=500, height=500, bg='white')
canvas.pack()
image = Image.open('/home/raja/Pictures/facebook/FB_IMG_14625555879653356.jpg')
photo = ImageTk.PhotoImage(image)
canvas.create_image(250, 250, image=photo)

root.mainloop()
