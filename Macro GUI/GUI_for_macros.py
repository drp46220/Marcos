from tkinter import *
from tkinter import ttk

def ScreenTest():
    root = TK()
    Frame = ttk.Frame(root, padding=5)
    Frame.grid()
    ttk.Label(Frame, text="test text").grid(column=0, row=1)
    ttk.Button(Frame, text="close", command=root.destroy).grid(column=3, row=0)
    root.mainLoop()

if __name__ == "__main__":
    ScreenTest()