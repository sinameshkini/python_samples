import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("%dx%d+%d+%d"%(300,200,100,50))
root.title('Tab test')

nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

f1 = tk.Frame(bg='red')
f2 = tk.Frame(bg='blue')
f3 = tk.Frame(bg='green')

nb.add(f1,text='page1')
nb.add(f2,text='page2')
nb.add(f3,text='page3')

btn1=tk.Button(f1,text='button1')
btn1.pack(side='left',anchor='nw',padx=50,pady=50)
root.mainloop()
