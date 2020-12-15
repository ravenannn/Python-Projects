import shutil
import os
import tkinter
from tkinter import *
from tkinter import filedialog
import datetime
import datetime as dt


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        self.master = master
        self.master.geometry("600x158")
        self.master.title('Check files')
        v = StringVar()

        #Create Browse Labels
        self.lblBrowse1 = Label(self.master,text="Choose Source: ", font=("Helvetica", 10), fg="black")
        self.lblBrowse1.grid(row=0, column=0, padx=(30, 0), pady=(15,0))

        self.lblBrowse2 = Label(self.master,text="Choose Destination: ", font=("Helvetica", 10), fg="black")
        self.lblBrowse2.grid(row=1, column=0, padx=(30, 0), pady=(15,0))

        #Create text boxes
        self.txtBrowse1 = Entry(self.master)
        # This command paints it onto the actual window
        self.txtBrowse1.grid(row=0,column=2, columnspan=3, padx=(30, 0), pady=(15,0), sticky=N+E+W)
        self.txtBrowse2 = Entry(self.master, text = "")
        self.txtBrowse2.grid(row=1,column=2, columnspan=3, padx=(30, 0), pady=(15,0), sticky=N+E+W)
        #Create buttons
        self.btnBrowse1 = Button(self.master, text="Browse...", width=12, height=1, command = self.browseFiles1)
        self.btnBrowse1.grid(row=0, column=1, padx=(30, 0), pady=(15,0))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=12, height=1, command = self.browseFiles2)
        self.btnBrowse2.grid(row=1, column=1, padx=(30, 0), pady=(15,0))
        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2, command = self.checkFiles)
        self.btnCheck.grid(row=2, column=2, padx=(30, 0), pady=(15,0))
        # Use command to call cancel function
        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.cancel)
        self.btnClose.grid(row=2, column=3, padx=(90, 0), pady=(15,0), sticky=N+E+W)
        
    # Create function for Browse1 to select Source Folder
    def browseFiles1(self):
        folderSelected1 = filedialog.askdirectory()
        print(folderSelected1)
        self.txtBrowse1.configure(state=NORMAL)
        self.txtBrowse1.delete(0, "end")
        self.txtBrowse1.insert(0, folderSelected1)
        self.txtBrowse1.configure(state=DISABLED)
        
                
    # Create function for Browse2 to select Destination folder
    def browseFiles2(self):
        folderSelected2 = filedialog.askdirectory()
        print(folderSelected2)
        self.txtBrowse2.configure(state=NORMAL)
        self.txtBrowse2.delete(0, "end")
        self.txtBrowse2.insert(0, folderSelected2)
        self.txtBrowse2.configure(state=DISABLED)
        
    # Create function to close/cancel window
    def cancel(self):
        self.master.destroy()



    def checkFiles(self):
        now = dt.datetime.now()
        ago = now-dt.timedelta(hours=24)

        #set where the source of the files are
        source = self.txtBrowse1.get()

        #set the destination path to folderB
        destination = self.txtBrowse2.get()


        for root, dirs, files in os.walk(source):
            for fname in files:
                path = os.path.join(root, fname)
                st = os.stat(path)
                mtime = dt.datetime.fromtimestamp(st.st_mtime)
                if mtime > ago:
                    shutil.copy2(path, destination)
          





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # Must use to continuously run
    root.mainloop()
