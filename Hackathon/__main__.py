from Application import *
import tkinter as tk

def main():
    app = Application(master=root)
    app.mainloop()
    print("end")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Test")
    root.geometry('1280x720')
    main()