from tkinter import Tk, Text, ttk, filedialog, messagebox, Menu, StringVar, Scrollbar, LEFT, RIGHT, Frame, VERTICAL


root = Tk();

frm = Frame(root);
frm.pack();

frm_2 = Frame(root);
frm_2.pack();

lbl = ttk.Label(frm, text = 'Lable_testing', background = 'green');
lbl.grid(row = 0, sticky="ew",);

lbl = ttk.Label(frm, text = 'Lable_testing', background = 'green');
lbl.grid(row = 0, column = 1, sticky="ew",);

txt = Text(frm_2, width = 40);
txt.grid(row = 1,sticky="ns")

scl = Scrollbar(frm_2, command = txt.yview);
scl.grid(row = 1, column = 1 , sticky="ns" );
txt.config(yscrollcommand = scl.set);



root.mainloop()
