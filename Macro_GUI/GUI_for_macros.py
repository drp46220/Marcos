import os
import tkinter
from tkinter import *
from tkinter import ttk
from GUI_Music import *
from GUI_Social import *
from GUI_VSC import *

def MainWindow():
    Main_Window = tkinter.Tk()
    Main_Window.title('Macro GUI')
    Frame = ttk.Frame(Main_Window, padding=10)
    Frame.grid()
    MusicBtn = ttk.Button(Frame, text="Music", command=lambda: Object.openAudio()).grid(column=1, row=0)
    SocialBtn = ttk.Button(Frame, text="Social", command=lambda: Object.openDiscord()).grid(column=1, row=1)
    EditorBtn = ttk.Button(Frame, text="Editor", command=lambda: Object.openVSC()).grid(column=1, row=2)
    Main_Window.mainloop()

if __name__ == "__main__":
    MainWindow()