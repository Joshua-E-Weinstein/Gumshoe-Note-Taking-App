import tkinter as tk

from DragDropMixin import DragDropMixin


class StickyNote(DragDropMixin, tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.create_window(150, 150, window=tk.Entry())
        self.place(x=0, y=0)


