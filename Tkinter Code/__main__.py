from Application import *
import tkinter as tk

def main():
    app = Application(master=root)  # Creates application based on root.
    app.mainloop()  # Runs application.
    print("end")


if __name__ == '__main__':

    # Makes the window's root and configures it.
    root = tk.Tk()
    root.title("Test")
    root.geometry('1280x720')
    # root.iconbitmap('')  # Change icon of window.
    root.minsize(700, 500)

    # Runs main.
    main()