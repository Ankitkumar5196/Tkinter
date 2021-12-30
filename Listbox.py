import tkinter as tk
from tkinter import ttk


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = tk.Tk()
root.title("Widget Examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

pl = tk.StringVar(value=programming_languages)
pl_select = tk.Listbox(root, listvariable=pl, height=6)
pl_select.pack(padx=10, pady=10)

pl_select["selectmode"] = "extended"  


def handle_selection_change(event):
    selected_indices = pl_select.curselection()
    for i in selected_indices:
        print(pl_select.get(i))


pl_select.bind("<<ListboxSelect>>", handle_selection_change)
root.mainloop()