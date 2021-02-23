import tkinter as tk

from DragDropMixin import DragDropMixin


class Map(DragDropMixin, tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.pack(side="right")