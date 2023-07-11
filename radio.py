import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Something something")
r=tk.IntVar()
r.set("1")

radios = []

lbl = tk.Label(root, text=r.get())

def updater():
    lbl.configure(text=r.get())


for n in range(5):
    radios.append(tk.Radiobutton(root, text=f"option {n+1}", variable=r , value=n+1, state=tk.NORMAL, command=updater))


for ra in radios:
    ra.pack()
lbl.pack()

root.mainloop()