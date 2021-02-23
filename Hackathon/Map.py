import tkinter as tk

class Map:
    def __init__(self, master=None, **kwargs):
        self.canvas = tk.Canvas(master, **kwargs)
        self.canvas.pack(side="right")