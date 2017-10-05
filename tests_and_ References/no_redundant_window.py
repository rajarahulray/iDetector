import tkinter as tk
from tkinter import ttk

def about_window(): 
    top2 = tk.Toplevel(root)
    top2.title("About")
    top2.resizable(0,0)

    explanation = "This program is my test program"

    ttk.Label(top2,justify=tk.LEFT,text=explanation).pack(padx=5,pady=2)
    ttk.Button(top2,text='OK',width=10,command=top2.destroy).pack(pady=8)

    top2.transient(root)
    top2.grab_set()
    top2.focus_set();
    root.wait_window(top2)

root = tk.Tk()
root.resizable(0,0)

root.style = ttk.Style()
# ('clam', 'alt', 'default', 'classic')
root.style.theme_use("clam")

menu = tk.Menu(root)
root.config(menu=menu)

fm = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Settings",menu=fm)
fm.add_command(label="Preferances")

hm = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help",menu=hm)
hm.add_command(label="About", command=about_window)
hm.add_command(label="Exit",command=root.quit)
#

tk.mainloop()
