import tkinter as tk

from Map import Map
from NiceButton import NiceButton
from StickyNote import StickyNote


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        button1 = NiceButton("top", master=self.master, text="print hi", command=(lambda: print("hi")))
        button2 = NiceButton("top", master=self.master, text="close window", command=(lambda: master.destroy()))
        sticky1 = StickyNote(master=self.master, text="Hello", bg="red")
        map = Map(master=self.master, bg="white", height=300, width=300)

    def say_hi(self):
        print("hi there, everyone!")
