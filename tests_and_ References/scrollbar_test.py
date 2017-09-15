from tkinter import Scrollbar, Tk, Text, LEFT, RIGHT

root = Tk();
txt_box = Text(root,)
txt_box.pack(side = LEFT);

srl = Scrollbar(root, command = txt_box.yview)
srl.pack(side = LEFT, fill = 'y');

txt_box.config(yscrollcommand = srl.set, )
root.mainloop();

'''Note....'''
'''scrollbar attaches itself to the textbox via command attribute in it set to
the yview or xview..and the position is decided according to the side specified i.e. either LEFT or RIGHT.
the last thing is to configure the text widget with the yscrollcommand  or xscrollcommand
having set to the <scrollbar_widget_object>.set

The srl.pack(side = LEFT, fill = 'y'); part is very importanat because in this the
side determines the side of the position of the scrollbar and the fill = 'y'
determines the filling of scrollbar in the region'''
