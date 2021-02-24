import tkinter as tk


class NiceButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.pack(side="top")

    # Function to pack the button to a frame.
    def packTo(self, frame):
        pass
