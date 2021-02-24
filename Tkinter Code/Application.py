import tkinter as tk

from Map import Map
from NiceButton import NiceButton
from StickyNote import StickyNote


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master

        # Buttons at top.
        printHi = NiceButton(master=self.master, text="print hi", command=(lambda: self.say_hi()))
        quitApp = NiceButton(master=self.master, text="close window", command=(lambda: master.destroy()))

        # Button in middle.
        test = NiceButton(master=self.master, text="500, 500", command=(lambda: print("x=500 y=500")))
        test.place(x=500, y=500)

        # Draggable top left.
        sticky1 = StickyNote(master=self.master, bg="white", height=300, width=300)

        # Canvas on right.
        googleMap = Map(master=self.master, bg="white", height=300, width=300)

    def say_hi(self):
        print("hi there, everyone!")
