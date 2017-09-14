#!/usr/bin/env python
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory


class Application:
    def selectLogFile(self):
        filename = askopenfilename()
        self.logFilePath.set(filename)

    def selectImageFile(self):
        imageFolder = askdirectory()
        self.imageFilePath.set(imageFolder)
        
    def __init__(self, master):
        frame = Frame(master,width=200,height=200)
        frame.pack()

        self.log_file_btn = Button(frame, text="Select Log File", command=self.selectLogFile,width=25).grid(row=0)
        self.image_folder_btn = Button(frame, text="Select Image Folder", command=self.selectImageFile,width=25).grid(row=1)
        self.quite_button = Button(frame, text="QUIT", fg="red", command=frame.quit,width=25).grid(row=5)

        self.logFilePath =StringVar()
        
        self.imageFilePath = StringVar()

        self.labelFolder = Label(frame,textvariable=self.logFilePath).grid(row=0,column=1)

        self.labelImageFile = Label(frame,textvariable = self.imageFilePath).grid(row = 1,column=1)

        

root = Tk()
root.title("Geo Tagging")
root.geometry("600x100")
app = Application(root)
root.mainloop()
