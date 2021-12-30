import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

root = tk.Tk()
root.title("Widget Examples")


initial_value = tk.IntVar(value=20)
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=initial_value,
    wrap=False)
spin_box.pack()

print(spin_box.get()) 

root.mainloop()