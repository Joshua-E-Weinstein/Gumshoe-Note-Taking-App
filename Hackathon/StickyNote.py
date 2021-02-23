import tkinter as tk

from DragDropMixin import DragDropMixin


class StickyNote(DragDropMixin, tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, kwargs)
        self.place(x=0, y=0)


