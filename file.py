import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

root = tk.Tk()


root.filename = filedialog.askopenfilename(initialdir=".", title="Select a file", filetypes=(("png files", "*.jpg"), ("all files", "*.*")))