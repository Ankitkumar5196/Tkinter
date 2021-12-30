import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=8) 
text.pack()

# Insert content into the text area
text.insert("1.0", "Please enter a comment...")

text["state"] = "normal" 

text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()