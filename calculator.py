import tkinter as tk
"""
This pp only sums because I don't feel like aking it do anything else, maybe I'll add more stuff later 
for now, this only sums
"""
root = tk.Tk()
root.title("Calculator")

ent = tk.Entry(root,  width=35, borderwidth=5, justify="right")
result = tk.Label(root, text="0", justify="right")

nums = []

def button_click(text):
    val=ent.get()+f"{text}"
    ent.delete(0, tk.END)
    ent.insert(0, val)

def button_clear():
    ent.delete(0, tk.END)
    result["text"]="0"
    global nums
    print(nums)
    nums=[]

def button_add():
    global nums
    print(nums)
    if ent.get().isdigit():
        nums.append(int(ent.get()))
    ent.delete(0, tk.END)
    result["text"]=sum(nums)
    nums=[sum(nums)]

button_sum = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
button_eq = tk.Button(root, text="=", padx=40, pady=20, command=button_add)
button_clear = tk.Button(root, text="Clear ", padx=125, pady=20, command=button_clear)


buttons=[]
for n in list(range(10)):
    btn = tk.Button(root, text=n, padx=40, pady=20, command=lambda x=n:button_click(x))
    buttons.append(btn)

ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
result.grid(row=1, column=2, columnspan=3)

buttons[7].grid(row=2, column=0)
buttons[8].grid(row=2, column=1)
buttons[9].grid(row=2, column=2)
                   
buttons[4].grid(row=3, column=0)
buttons[5].grid(row=3, column=1)
buttons[6].grid(row=3, column=2)

buttons[1].grid(row=4, column=0)
buttons[2].grid(row=4, column=1)
buttons[3].grid(row=4, column=2)

buttons[0].grid(row=5, column=0)
button_sum.grid(row=5, column=1)
button_eq.grid(row=5, column=2)

button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()