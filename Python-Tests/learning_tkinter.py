
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        # master is the colored box/window we are creating
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg="lightgray")

        # Creating text strings
        self.varFName = StringVar()
        self.varLName = StringVar()
##        self.varFName.set("Bob")
##        self.varLName.set("Smith")
##
##        # print to the console for the dev to see and test, not the user
##        print(self.varFName.get())
##        print(self.varLName.get())

        self.lblFName = Label(self.master,text="First Name: ", font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblFName.grid(row=1, column=0, padx=(30, 0), pady=(30,0))

        self.lblLName = Label(self.master,text="Last Name: ", font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblLName.grid(row=0, column=0, padx=(30, 0), pady=(30,0))

        self.lblDisplay = Label(self.master,text="", font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblDisplay.grid(row=3,column=1, padx=(30, 0), pady=(30,0))
        
        # self.master is the colored box we created
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg="black", bg="lightblue")
        # This command paints it onto the actual window
        self.txtFName.grid(row=0,column=1, padx=(30, 0), pady=(30,0))
        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg="black", bg="lightblue")
        self.txtLName.grid(row=1,column=1, padx=(30, 0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1, padx=(0, 0), pady=(30,0), sticky=NE)
        
        self.btnCancel= Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(0, 90), pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text="Hello, {} {}!".format(fn,ln))

    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # Must use to continuously run
    root.mainloop()
