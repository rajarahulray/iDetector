from tkinter import Tk, Scrollbar, Label, Frame;

root = Tk();
root.config(background = 'blue')

frm_1 = Frame(root);
frm_1.grid(row = 0, column = 0, sticky = 'nsew');

frm_2 = Frame(root);
frm_2.grid(row = 1, column = 0, sticky = 'nsew');

lbl_frm_1 = Label(frm_1, text = 'something', width = 20, height = 20, bg = 'white')
lbl_frm_1.grid(row = 0, column = 0, sticky = 'nsew');

scl_bar_lbl_frm_1 = Scrollbar(frm_1, command = lbl_frm_1.yview);
scl_bar_lbl_frm_1.grid(row = 0, column = 1, sticky = 'nsew');
lbl_frm_1.config(yscrollcommand = scl_bar_lbl_frm_1.set);

tmp_lbl_frm_2 = Label(frm_2, bg = 'yellow',width = 20, height = 20)
tmp_lbl_frm_2.grid(row = 0, column = 0, sticky = 'nsew');

root.mainloop();
