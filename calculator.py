import tkinter as tk

root = tk.Tk()
root.title("Calculator")

ent = tk.Entry(root, width=35, borderwidth=5)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)