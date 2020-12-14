Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> v = StringVar()
>>> e = Entry(win, textvariable = v)
>>> e.pack()
>>> v.get()
'This is a test'
>>> v.set("this is set by the program")
>>> 