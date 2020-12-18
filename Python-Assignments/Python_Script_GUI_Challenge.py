
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        self.master = master
        self.master.geometry("531x158")
        self.master.title('Check files')

        #Create text boxes
        self.txtBrowse1 = Entry(self.master, text='')
        # This command paints it onto the actual window
        self.txtBrowse1.grid(row=0,column=1, columnspan=3, padx=(30, 0), pady=(15,0), sticky=N+E+W)
        self.txtBrowse2 = Entry(self.master, text='')
        self.txtBrowse2.grid(row=1,column=1, columnspan=3, padx=(30, 0), pady=(15,0), sticky=N+E+W)
        #Create buttons
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=(30, 0), pady=(15,0))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(30, 0), pady=(15,0))
        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(30, 0), pady=(15,0))
        self.btnClose = Button(self.master, text="Close Program", width=12, height=2)
        self.btnClose.grid(row=2, column=3, padx=(90, 0), pady=(15,0), sticky=NE)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # Must use to continuously run
    root.mainloop()
