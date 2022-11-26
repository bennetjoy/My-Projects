import tkinter as tk     #for referencee check https://realpython.com/python-gui-tkinter/
from tkinter import *
import _tkinter
gui = Tk(className='Belle')
gui.geometry("500x200")
#top = tk.Tk()   if there is no gui
label = tk.Label(text="Hello, Tkinter", foreground="white", background="black", width=20, height=10)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()
button.pack()
label.pack()
 #top.mainloop()   if there is no gui 
gui.mainloop()

