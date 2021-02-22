import tkinter as tk


class NiceButton:
    def __init__(self, text, command, master=None):
        self.button = tk.Button(master)
        self.button["text"] = text
        self.button["command"] = command
        self.button.pack(side="top")