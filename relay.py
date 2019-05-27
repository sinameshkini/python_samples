import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

status = [("OFF"),("ON")]

def ShowChoice():
    if v.get()==0:
        print("is off")
    else:
        print("in on")


for val, status in enumerate(status):
    tk.Radiobutton(root,
                  text=status,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()
