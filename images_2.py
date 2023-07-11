import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image
import os #this is a special tool that will help us later

root = tk.Tk()
root.geometry("800x600")
root.config(background="#393D47")
#I'm creating a frame to separate buttons from label
top_frame = tk.Frame(root)
top_frame.configure(background="#393D47", padx=10, pady=10)#I love that color

imgs = []
#this checks the selected folder and scans all image files(supported by pillow) and creates a list of ImageTk objects
for item in os.listdir(".\images"):
    #any not img file crashes the previous way
    #This is the way
    try:
        imgs.append(ImageTk.PhotoImage(Image.open(f"images\{item}")))
    except Exception as e:
        print(e)

size = len(imgs)
current_index = 0

#creates the label with the first image, this is the one we'll be changing
my_label=tk.Label(image=imgs[current_index], borderwidth=0, padx=30, pady=30,border=50, background="#393D47")

#this sets all buttons to normal then, if the image is first or last , it will disable a button
def states():
    button_back.configure(state=tk.NORMAL) 
    button_front.configure(state=tk.NORMAL)
    if current_index==0:
        button_back.configure(state=tk.DISABLED)
    if current_index == size-1:
        button_front.configure(state=tk.DISABLED)

def move(dir):
    #this just changes the image that should be displayed
    global current_index
    if dir =="<<":
        current_index -=1
        my_label["image"]=imgs[current_index]
        
    elif dir == ">>":
        current_index +=1
        my_label["image"]=imgs[current_index]
    
    #Running this will block the button when needed
    states()



button_back = ttk.Button(top_frame, text="<<", command=lambda x="<<":move(x) , padding=10)
button_front = ttk.Button(top_frame, text=">>", command=lambda x=">>":move(x), padding=10)
button_quit= ttk.Button(top_frame, text="Exit", command=root.quit, padding=10)

#Running it at start for good measure
states()

#packing all the stuff
top_frame.pack()
button_back.pack(side="left")
button_front.pack(side="right")
button_quit.pack()
my_label.pack()

root.mainloop()