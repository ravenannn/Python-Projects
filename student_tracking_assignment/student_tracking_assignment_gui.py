##Python Ver:     3.9
##
##Author:         Raven A. Sumner
##
##Purpose:        Create a student tracking system application
##                using Python with Tkinter and SQLLite3
##
##Tested OS:      This code was written and tested to work with
##                Windows 10.


from tkinter import *
import tkinter as tk

# Be sure to import our other modules 
# so we can have access to them
import student_tracking_assignment_main
import student_tracking_assignment_func



def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """
    self.lblFName = Label(self.master,text="First Name: ", font=("Helvetica", 16), fg="black", bg="#F0F0F0")
    self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30,0))
    self.lblLName = Label(self.master,text="Last Name: ", font=("Helvetica", 16), fg="black", bg="#F0F0F0")
    self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30,0))
    self.lblPhone = Label(self.master,text="Phone Number: ", font=("Helvetica", 16), fg="black", bg="#F0F0F0")
    self.lblPhone.grid(row=2, column=0, padx=(30, 0), pady=(30,0))
    self.lblEmail = Label(self.master,text="Email Address: ", font=("Helvetica", 16), fg="black", bg="#F0F0F0")
    self.lblEmail.grid(row=3, column=0, padx=(30, 0), pady=(30,0))
    self.lblCourse = Label(self.master,text="Current Course: ", font=("Helvetica", 16), fg="black", bg="#F0F0F0")
    self.lblCourse.grid(row=4, column=0, padx=(30, 0), pady=(30,0))

##    self.lblDisplay = Label(self.master,text="", font=("Helvetica", 16), fg="black", bg="lightgray")
##    self.lblDisplay.grid(row=3,column=1, padx=(30, 0), pady=(30,0))
        
    # self.master is the colored box we created
    self.txtFName = tk.Entry(self.master,text='', font=("Helvetica", 16), fg="black", bg="lightgray")
    # This command paints it onto the actual window
    self.txtFName.grid(row=0,column=1, padx=(30, 0), pady=(30,0))
    self.txtLName = tk.Entry(self.master,text='', font=("Helvetica", 16), fg="black", bg="lightgray")
    self.txtLName.grid(row=1,column=1, padx=(30, 0), pady=(30,0))
    self.txtPhone = tk.Entry(self.master,text='', font=("Helvetica", 16), fg="black", bg="lightgray")
    self.txtPhone.grid(row=2,column=1, padx=(30, 0), pady=(30,0))
    self.txtEmail = tk.Entry(self.master,text='', font=("Helvetica", 16), fg="black", bg="lightgray")
    self.txtEmail.grid(row=3,column=1, padx=(30, 0), pady=(30,0))
    self.txtCourse = tk.Entry(self.master,text='', font=("Helvetica", 16), fg="black", bg="lightgray")
    self.txtCourse.grid(row=4,column=1, padx=(30, 0), pady=(30,0))

    self.btnSubmit = tk.Button(self.master, text="Submit", width=10, height=2, command=lambda: student_tracking_assignment_func.addToList(self))
    self.btnSubmit.grid(row=6,column=1, padx=(25, 0), pady=(45,10), sticky=NW)
    self.btn_delete = tk.Button(self.master,width=10,height=2,text='Delete',command=lambda: student_tracking_assignment_func.onDelete(self))
    self.btn_delete.grid(row=6,column=1,padx=(15,0),pady=(45,10),sticky=NE)
  


    student_tracking_assignment_func.create_db(self)
    student_tracking_assignment_func.onRefresh(self)

    



if __name__ == "__main__":
    pass
