import tkinter as tk


x_cor = 10;
y_cor = 5;

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in txt
    txt.configure(scrollregion=txt.bbox('all'))


root = tk.Tk()


l = tk.Label(root, text="Hello", font="-size 50")
l.pack()
# --- create txt with scrollbar ---

txt = tk.Text(root,width = 40)
txt.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=txt.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

txt_2 = tk.Text(root, width = 40);
txt_2.place(x = x_cor + 390, y = y_cor + 85);

scrollbar_2 = tk.Scrollbar(root, command=txt_2.yview)
scrollbar_2.pack(side=tk.RIGHT, fill='y')

txt.configure(yscrollcommand = scrollbar.set)
txt_2.configure(yscrollcommand = scrollbar_2.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in txt
#txt.bind('<Configure>', on_configure)

# --- put frame in txt ---

frame = tk.Frame(txt, width=768, height=576, bg="", colormap="new")
frame.pack()
frame_2 = tk.Frame(txt_2);
frame_3 = tk.Frame(l);
#txt.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---

l = tk.Label(frame, text="Hello", font="-size 50")
l.pack()

l = tk.Label(frame, text="World", font="-size 50")
l.pack()

l = tk.Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
l.pack()

# --- start program ---

root.mainloop()
