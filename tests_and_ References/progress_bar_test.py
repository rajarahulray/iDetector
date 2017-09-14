from tkinter import *
from tkinter import ttk

root = Tk();

pr = ttk.Progressbar(root, orient = 'horizontal', length = 200, mode = 'determinate');
pr.pack();

root.mainloop();

