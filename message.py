import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("the title")
#maybe I should add an icon

def popup():
    #messagebox.showinfo("Stop, see the info", "This is the info")
    #messagebox.showwarning("WARNING!", "This is the warning!")
    #messagebox.askquestion("Question", "really?")
    #messagebox.showerror("ERROR!", "This is an error")
    resp = messagebox.askokcancel("Question", "are you sure?")
    print(resp)
    """
    dir(messagebox):
    ['ABORT', 'ABORTRETRYIGNORE', 'CANCEL', 'Dialog', 'ERROR', 'IGNORE', 'INFO', 'Message', 'NO', 'OK', 'OKCANCEL', 'QUESTION', 'RETRY', 'RETRYCANCEL', 'WARNING', 'YES', 
    'YESNO', 'YESNOCANCEL', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_show', 'askokcancel', 'askquestion', 'askretrycancel', 'askyesno', 'askyesnocancel', 'showerror', 'showinfo', 'showwarning']
    """

btn = tk.Button(root, text="Pupup", command=popup)

btn.pack()




root.mainloop()