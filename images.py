import tkinter as tk

root = tk.Tk()
root.title("Images")
root.geometry("850x500")
root.iconbitmap("images/dollar.ico")

# subsample divides image size by refferenced scale
#I know there is a TILish way but I want to know this before filling up the ram with random libraries I'll use only once
valar_morghulis = tk.PhotoImage(file="images/valar_morghulis.png").subsample(2,2)
valar_dohaeris = tk.PhotoImage(file="images/valar_dohaeris.png")


lbl = tk.Label(root, image=valar_morghulis,borderwidth=2, relief="solid")
def changer():
    lbl["image"]=valar_dohaeris

button_quit=tk.Button(root, text="Change image", command= changer)

button_quit.pack()
lbl.pack()

root.mainloop()