import tkinter as tk


class NiceButton(tk.Button):
    def __init__(self, side, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.pack(side=side)
