from Tkinter import *

root = Tk()
logo = PhotoImage(file="/home/dakhou/bin/images/Dakhou.jpg")
w1 = Label(root, image=logo).pack(side="right")
explanation = """Sina is Dakhou """
w2 = Label(root,
		justify=LEFT,
		padx = 10,
		text=explanation).pack(side="left")
root.mainloop()
