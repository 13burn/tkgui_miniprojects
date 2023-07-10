import tkinter as tk

class Window(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # tk.Frame.__init__ creates self.master so you don't have to
        #self.master = master 

        self.init_window()

    def init_window(self):
        self.pack(fill=tk.BOTH, expand=1)

        quit_button = tk.Button(self, text="Exit", command=root.destroy)
        start_button = tk.Button(self, text="Browse", command=self.on_click)

        self.label = tk.Label(self, text="Hello")

        quit_button.grid(row=0, column=0)
        start_button.grid(row=0, column=1)

        self.label.grid(row=1, column=0, columnspan=2)

    def on_click(self):
        self.label['text'] = "Starting..."

root = tk.Tk()
app = Window(root)
root.mainloop()