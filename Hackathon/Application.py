import tkinter as tk
from NiceButton import NiceButton


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        button = NiceButton("print hi", lambda: print("hi"), master=self.master)

    def say_hi(self):
        print("hi there, everyone!")
