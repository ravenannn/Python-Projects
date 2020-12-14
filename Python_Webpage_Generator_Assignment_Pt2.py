
import tkinter
from tkinter import *
import os
import webbrowser


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        # master is the colored box/window we are creating
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 200))
        self.master.title('Set Your Own Text')
        self.master.config(bg="lightgray")

        # Creating text strings
        self.varNewText = StringVar()
        # Create label for text box
        self.lblNewText = Label(self.master,text="New Text for Web Page: ", font=("Helvetica", 16), fg="black", bg="lightgray")
        self.lblNewText.grid(row=1, column=0, padx=(30, 0), pady=(30,0))
        # Create text box for entry
        self.txtNewText = Entry(self.master,text=self.varNewText, font=("Helvetica", 16), fg="black", bg="lightblue")
        # This command paints it onto the actual window
        self.txtNewText.grid(row=1,column=1, padx=(30, 0), pady=(30,0))
        # Create button to submit user's desired text
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1, padx=(0, 0), pady=(30,0), sticky=NE)

    def submit(self):
        newText = self.varNewText.get()
        with open("webpage.html", "w") as f:
            f.write("<html>\n\t<body>\n\t\t<h1>\n\t\t  {}\n\t\t</h1>\n\t</body>\n</html>".format(newText))
            f.close()
        webbrowser.open_new_tab("webpage.html")


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # Must use to continuously run
    root.mainloop()
