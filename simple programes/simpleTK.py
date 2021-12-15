import tkinter
from tkinter import *

#create a window...
window=Tk()

#title of the window...
window.title("sample window")

#the size of window
window.geometry("400x200")

#create a simple text inside of the window 
l1=Label(window,text="hello world").pack()

#create a simple button
b1=Button(window,text="click me")#here also use .pack()
b1.pack()#this is alternative

#now run the window
window.mainloop()
