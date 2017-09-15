from Tkinter import * #Import the Tkinter module
from ScrolledText import ScrolledText #import the scrolled text module
message = "I \n am \n scroll \n able. \n\n\n\n\n\n Yes I am!"
class Application(Frame): #Create a frame for the widgets

    def __init__(self, master):  #initialize the grid and widgets
        Frame.__init__(self,master)
        self.grid()
        self.widgets()
    def widgets(self):
        self.mytext = ScrolledText(self, width = 10) #Creates the widget
        self.mytext.grid() #Places it


root = Tk()
root.title("My Text Example")
#make my screen dimensions work

root.geometry("500x1000")
app = Application(root)

root.mainloop()


#not working..
