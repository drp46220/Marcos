import os
import tkinter
from tkinter import *
from tkinter import ttk
import Music_Marco

def MainWindow():
    Main_Window = tkinter.Tk()
    Main_Window.title('Macro GUI')
    Frame = ttk.Frame(Main_Window, padding=10)
    Frame.grid()
    ttk.Button(Frame, text="Music", command=Music_Marco.openAudio()).grid(column=1, row=0)
    Main_Window.mainloop()

if __name__ == "__main__":
    MainWindow()