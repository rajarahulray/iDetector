import tkinter as tk
import os
import tkinter.filedialog
import tkinter.messagebox

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        '''This initialisation runs the whole program'''
        #textBoxList = []

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Untitled')
        self.geometry('500x500')
        self.canvas = tk.Canvas(self)
        self.scroll = tk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.frame = tk.Frame(self.canvas) # frame does not get pack() as it needs to be embedded into canvas throught canvas.
        self.scroll.pack(side='right', fill='y')
        self.canvas.pack(fill='both', expand='yes')
        self.canvas.create_window((0,0), window=self.frame, anchor='nw')
        self.frame.bind('<Configure>', lambda x: self.canvas.configure(scrollregion=self.canvas.bbox('all'))) # lambda function

        # 1st Text Widget
        self.journal = tk.Text(self.frame)
        self.vsb = tk.Scrollbar(self.frame)
        self.vsb.config(command=self.journal.yview)
        self.journal.config(yscrollcommand=self.vsb.set)
        self.journal.grid(row=0, column=0) # grid instead
        self.vsb.grid(row=0, column=1, sticky='ns') # grid instead

        #2nd Text Widget
        self.good = tk.Text(self.frame)
        self.vsb2 = tk.Scrollbar(self.frame)
        self.vsb2.config(command=self.good.yview)
        self.good.config(yscrollcommand=self.vsb2.set)
        self.good.grid(row=1, column=0) # grid instead
        self.vsb2.grid(row=1, column=1, sticky='ns') # grid instead

root = Main()
root.mainloop()
