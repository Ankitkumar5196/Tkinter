import tkinter as tk
from tkinter import ttk

root=tk.Tk()
style=ttk.Style(root)
print(style.theme_names())
root.mainloop()