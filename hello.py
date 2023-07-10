from tkinter import ttk
import tkinter as tk
print(dir(tk.ttk))

root = tk.Tk()

#I'm creating frames becasue I can give thos style
label_frame = ttk.LabelFrame(root)#, background="#010203", width=200, height=125, padx=50, pady=50)
button_frame = tk.LabelFrame(root, background="#aaaaaa", width=200, height=125, padx=50, pady=50)

#I need to declare this before the functions because they crash, It will be solved with a class
ent = tk.Entry(button_frame )

#this function appends a new label to the frame (slaves) and deletes the first one 
#basically is a replacement
def click():
    txt = ent.get()
    click_label =tk.Label(label_frame, text=txt ).pack()
    label_frame.pack_slaves()[0].destroy()
    #root.pack_slaves()[1].destroy()#this breaks my code with entry

#this function does the exact thing as the other one but in a different way (I know, I know)
def writter():
    txt = ent.get()
    click_label =tk.Label(label_frame)
    click_label["text"] = txt
    label_frame.pack_slaves()[0].destroy()
    click_label.pack()

#just a bunch of stuff that I like but don't want to use    
#root.title("Awesome")
#label = tk.Label(root, text="this is the label").pack()
"""
lframe = tk.LabelFrame(root, text="frame").grid(row=0, column=0, padx=10, pady=10)
label1 = tk.Label(lframe, text="The label").grid(row=0,column=0)
label2 = tk.Label(lframe, text="The label").grid(row=1,column=1)
"""

button1 = ttk.Button(button_frame, text="Click me!",  command=click )
label1 = ttk.Label(label_frame, text="The label")

#this will call the function when the key (any key) is released but only when the entry is selected
ent.bind("<KeyRelease>", lambda event: writter())
#ent.bind("<KeyRelease>", lambda k:writter)

#packing all the meat
button_frame.pack(side="top")
label_frame.pack(side="bottom" )
button1.pack()
label1.pack()
ent.pack()

#the main loop --this one is important--
root.mainloop()