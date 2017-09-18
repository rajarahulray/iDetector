from tkinter import Tk, Text, ttk, filedialog, messagebox, Menu, StringVar, Scrollbar, LEFT, RIGHT, Frame, WORD, NONE

from astropy.table import Table, Column

import terminaltables as tb

table_data = [
    ['Sr. No.', 'Name', 'Value', ],
    ['1', 'Person', '98.23211',],
    ['2', 'People', '96.13245'],
    ['3', 'Awesome', '88.3254'],
    ['']
]
table = tb.DoubleTable(table_data)
print (table.table);



##tab = Table()
##tab['a'] = [1, 4]
##tab['b'] = Column([2.0, 5.0], unit='cm', description='Velocity')
##tab['c'] = ['x', 'y']
##
##print(tab);


root = Tk();
#root.geometry('300x300');

#___________________________________________
frm_1 = Frame(root, background = 'green');
frm_1.grid(row = 0, columnspan = 5, sticky = 'ew');

l = ttk.Label(frm_1, text = 'ALpha', background = 'blue').grid(row = 1, column =1, sticky = 'nsew');

frm_1.grid_rowconfigure(0, weight=1)
frm_1.grid_rowconfigure(2, weight=1)
frm_1.grid_columnconfigure(0, weight=1)
frm_1.grid_columnconfigure(2, weight=1)

#l = ttk.Label(frm_1, text = 'ALpha').grid(row = 0, sticky = 'ew');

#___________________________
frm_2 = Frame(root);
frm_2.grid(row = 1, column = 0, sticky = 'nsew');


scl_t_y = Scrollbar(frm_2,);
scl_t_y.grid(row = 0, column =1, sticky = 'nsew');

scl_t_x = Scrollbar(frm_2, orient = 'horizontal');
scl_t_x.grid(row = 1, column = 0, sticky = 'nsew');

t = Text(frm_2, wrap = NONE, yscrollcommand = scl_t_y.set, xscrollcommand = scl_t_x.set,\
         background = 'silver', foreground = 'brown');
t.grid(row = 0, column = 0);

scl_t_x.config(command = t.xview);
scl_t_y.config(command = t.yview);

t.insert('insert',  'Image Name: \n');

t.insert('insert',  table.table);

l = ttk.Label(frm_2,)
l.grid(row = 0, column = 2);

##print(root.bbox())

##for i in range(5):
##    print(root.bbox(0,i));
##    print(root.bbox(1,i));

#___________________________________
frm_3 = Frame(root);
frm_3.grid(row = 1, column = 4, sticky = 'ns');

t2 = Text(frm_3);
t2.grid(row = 0,sticky = 'ns');

scl_t2 = Scrollbar(frm_3, command = t2.yview);
scl_t2.grid(row = 0, column =1, sticky = 'ns');
t2.config(yscrollcommand = scl_t2.set);

#_________________________image_label________
#
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.mainloop();
