import tkinter as tk

root = tk.Tk()
root.title("Calculator")

ent = tk.Entry(root,  width=35, borderwidth=5)

nums = []

def button_click(text):
    val=ent.get()+f"{text}"
    ent.delete(0, tk.END)
    print(val)
    ent.insert(0, val)

def btn_clear():
    ent.delete(0, tk.END)
    global nums
    nums=[]

def button_add():
    if ent.get():
        print(ent.get())
        nums.append(int(ent.get()))
        ent.delete(0, tk.END)
        print(sum(nums) )

button_sum = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
button_eq = tk.Button(root, text="=", padx=40, pady=20, command=lambda: print(root.winfo_reqwidth()))
button_clear = tk.Button(root, text="Clear ", padx=125, pady=20, command=btn_clear)


buttons=[]
for n in list(range(10)):
    btn = tk.Button(root, text=n, padx=40, pady=20, command=lambda x=n:button_click(x))
    buttons.append(btn)

print(buttons)

ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)
                   
buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)

buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)

buttons[0].grid(row=4, column=0)
button_sum.grid(row=4, column=1)
button_eq.grid(row=4, column=2)

button_clear.grid(row=5, column=0, columnspan=3)

root.mainloop()