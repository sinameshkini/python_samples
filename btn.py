import Tkinter as tk

def sina():
    print "sina"

root = tk.Tk()

label = tk.Label(root,fg="green")
label.pack()

button = tk.Button(root,text='stop',width=25,command=sina)
button.pack()

root.mainloop()
