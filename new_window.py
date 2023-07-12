import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.bell()
root.title("This is the title")

fr = tk.Frame(root)

img = ImageTk.PhotoImage(Image.open("images\\valar_morghulis.jpg"))

#I need to learn how to block root frome activating a ne one..., maybe just the button, this might be better with classes
def enable(top):
    btn.config(state=tk.NORMAL) 
    top.destroy()

def open():
    top=tk.Toplevel(root)
    top.wm_attributes("-topmost", 1)
    label = tk.Label(top, image=img)
    btn.config(state=tk.DISABLED)
    top.protocol("WM_DELETE_WINDOW", func=lambda x=top: enable(x))
    label.pack()


btn = tk.Button(fr, text="open second window", command=open)

fr.pack()
btn.pack()



root.mainloop()